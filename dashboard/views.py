from datetime import datetime
from django.db.models import Sum

from rest_framework import views, permissions, status

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from lib.response import Response
from lib.render_to_pdf import render_to_pdf
from income_app.models import Income
from expense_app.models import Expense
from expense_app.serializers.expense_serializer import ExpenseSerializer
from income_app.serializers.income_serializer import IncomeSerializer
from budget_app.models import TotalBudget

from user_app.models import UserProfile
from notifications.services import EmailServices

from dashboard.docs import schema_examples

from drf_yasg.utils import swagger_auto_schema

class DashboardView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            schema_examples.MONTHS_PARAMS,
        ],
        operation_description="Get dashboard data",
        operation_summary="Get dashboard data",
        tags=["Dashboard"],
        responses=schema_examples.DASHBOARD_RESPONSE,
    )
    def get(self, request):
        user = request.user
        current_month = datetime.now().month
        month_id = request.GET.get("month", datetime.now().month)

        # TOTAL TRANSACTIONS
        income_qs = Income.objects.filter(
            owner=user, income_date__month=month_id)
        expense_qs = Expense.objects.filter(
            owner=user, expense_date__month=month_id)

        total_transaction = income_qs.count() + expense_qs.count()

        # SUM OF INCOME
        sum_of_income = income_qs.aggregate(Sum('amount'))

        # SUM OF EXPENSES
        sum_of_expenses = expense_qs.aggregate(Sum('amount'))

        sum_of_expenses_amount = sum_of_expenses['amount__sum'] if sum_of_expenses['amount__sum'] else 0
        sum_of_income_amount = sum_of_income['amount__sum'] if sum_of_income['amount__sum'] else 0

        available_balance = sum_of_income_amount - sum_of_expenses_amount

        # TOP 3 INCOMES
        all_income = income_qs.order_by('-amount')
        all_income_serialized = IncomeSerializer(all_income, many=True)


        # TOP 3 EXPENSES
        all_expense = expense_qs.order_by('-amount')
        all_expense_serialized = ExpenseSerializer(all_expense, many=True)

        days_income = [0] * 31
        days_expense = [0] * 31
        days_label = [i for i in range(1, 32)]

        # INCOME GRAPH DATA
        income_dict = {}
        for i in all_income:
            income_dict[i.income_date.day] = i.amount

        income_days = [i.income_date.day for i in all_income]

        for k, v in income_dict.items():
            days_income[k-1] = v


        #EXPENSE GRAPH DATA
        expense_dict = {}
        for i in all_expense:
            expense_dict[i.expense_date.day] = i.amount

        expense_days = [i.expense_date.day for i in all_expense]

        for k, v in expense_dict.items():
            days_expense[k-1] = v


        user_profile = UserProfile.objects.filter(user=request.user).first()
        user_currency = user_profile.prefered_currency if user_profile else "$"


        results = {
            "total_transaction": total_transaction,
            "sum_of_income": sum_of_income_amount,
            "sum_of_expenses": sum_of_expenses_amount,
            "available_balance": available_balance,
            "currency":user_currency,
            "top_income": all_income_serialized.data[0:4],
            "top_expense": all_expense_serialized.data[0:4],
            "income_graph_data": days_income,
            "expense_graph_data": days_expense,
            "days_label":days_label
        }

        return Response(data=results, status=status.HTTP_200_OK)


class ReportView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, month_id, year_id):
        user = request.user
        current_month = datetime.now().month
        current_year = datetime.now().year

        user_profile = UserProfile.objects.filter(user=user).first()
        currency = user_profile.prefered_currency if user_profile else '$'

        # TOP 3 INCOMES
        all_income = Income.objects.filter(
            owner=user, income_date__month=month_id, income_date__year=year_id).order_by('-created_at')
        all_income_serialized = IncomeSerializer(all_income, many=True)

        # TOP 3 EXPENSES
        all_expense = Expense.objects.filter(
            owner=user, expense_date__month=month_id,expense_date__year=year_id,).order_by('-created_at')
        all_expense_serialized = ExpenseSerializer(all_expense, many=True)
        # SUM OF INCOME
        sum_of_income = Income.objects.filter(
            owner=user, income_date__month=month_id, income_date__year=year_id).aggregate(Sum('amount'))

        # SUM OF EXPENSES
        sum_of_expenses = Expense.objects.filter(
            owner=user, expense_date__month=month_id, expense_date__year=year_id).aggregate(Sum('amount'))

        sum_of_expenses_amount, sum_of_income_amount = 0, 0

        sum_of_expenses_amount = sum_of_expenses['amount__sum'] if sum_of_expenses['amount__sum'] else 0
        sum_of_income_amount = sum_of_income['amount__sum'] if sum_of_income['amount__sum'] else 0
        available_balance = sum_of_income_amount - sum_of_expenses_amount

        total_budget_income, total_budget_expense, total_budget_balance = (0, 0, 0)

        total_budget = TotalBudget.objects.filter(owner=user, month=month_id).first()
        if total_budget:
            total_budget_income = total_budget.total_budget_income
            total_budget_expense = total_budget.total_budget_expense
            total_budget_balance = total_budget.total

        datetime_object = datetime.strptime(str(month_id), "%m")
        month_name = datetime_object.strftime("%b")
        full_month_name = datetime_object.strftime("%B")


        context={
                "all_expense":all_expense_serialized.data,
                "total_expense":sum_of_expenses_amount,
                "all_income":all_income_serialized.data,
                "total_income":sum_of_income_amount,
                "available_balance":available_balance,
                "month":month_name,
                "year":year_id,
                "full_month_name":full_month_name,
                "budget_income":total_budget_income if year_id == str(current_year) else None,
                "budget_expenses":total_budget_expense if year_id == str(current_year) else None,
                "budget_balance":total_budget_balance if year_id == str(current_year) else None,
                "currency":currency
            }

        return Response(
            data=context,
            status=status.HTTP_200_OK
        )


def get_report_context(user):
    current_month = datetime.now().month
    user_profile = UserProfile.objects.filter(user=user).first()
    currency = user_profile.prefered_currency if user_profile else '$'

    # EXPENSES && INCOME QUERY
    expense_qs = Expense.objects.filter(owner=user, income_date__month=current_month)
    income_qs = Income.objects.filter(owner=user, income_date__month=current_month)

    # TOP 3 INCOMES
    all_income = income_qs.order_by('-created_at')
    all_income_serialized = IncomeSerializer(all_income, many=True)

    # TOP 3 EXPENSES
    all_expense = expense_qs.order_by('-created_at')
    all_expense_serialized = ExpenseSerializer(all_expense, many=True)

    # SUM OF INCOME
    sum_of_income = income_qs.aggregate(Sum('amount'))

    # SUM OF EXPENSES
    sum_of_expenses = expense_qs.aggregate(Sum('amount'))

    sum_of_expenses_amount = sum_of_expenses['amount__sum'] if sum_of_expenses['amount__sum'] else 0
    sum_of_income_amount = sum_of_income['amount__sum'] if sum_of_income['amount__sum'] else 0
    available_balance = sum_of_income_amount - sum_of_expenses_amount

    total_budget = TotalBudget.objects.filter(owner=user, month=current_month).first()
    total_budget_income = total_budget.total_budget_income if total_budget else 0
    total_budget_expense = total_budget.total_budget_expense if total_budget else 0
    total_budget_balance = total_budget.total if total_budget else 0


    datetime_object = datetime.strptime(str(current_month), "%m")
    month_name = datetime_object.strftime("%b")
    full_month_name = datetime_object.strftime("%B")

    context={
            "all_expense":all_expense_serialized.data,
            "total_expense":sum_of_expenses_amount,
            "all_income":all_income_serialized.data,
            "total_income":sum_of_income_amount,
            "available_balance":available_balance,
            "month":month_name,
            "full_month_name":full_month_name,
            "budget_income":total_budget_income,
            "budget_expenses":total_budget_expense,
            "budget_balance":total_budget_balance,
            "currency":currency
        }
    EmailServices.send_async(
        template="report.html",
        subject=f"Fintrak {full_month_name} Report",
        recipients=[user.email],
        context=context
    )
    return context

class GeneratePDF(views.APIView):
    def get(self, request, *args, **kwargs):
        template = get_template('report.html')
        context = get_report_context(request.user)
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

class NewGeneratePdf(views.APIView):
    def get(self, request, *args, **kwargs):
        data = get_report_context(request.user)
        pdf = render_to_pdf('report.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

def generate_report(user):
    current_month = datetime.now().month
    user_profile = UserProfile.objects.filter(user=user).first()
    currency = user_profile.prefered_currency if user_profile else '$'

    # TOP 3 INCOMES
    all_income = Income.objects.filter(
        owner=user, income_date__month=current_month).order_by('-created_at')
    all_income_serialized = IncomeSerializer(all_income, many=True)

    # TOP 3 EXPENSES
    all_expense = Expense.objects.filter(
        owner=user, expense_date__month=current_month).order_by('-created_at')
    all_expense_serialized = ExpenseSerializer(all_expense, many=True)
    # SUM OF INCOME
    sum_of_income = Income.objects.filter(
        owner=user, income_date__month=current_month).aggregate(Sum('amount'))

    # SUM OF EXPENSES
    sum_of_expenses = Expense.objects.filter(
        owner=user, expense_date__month=current_month).aggregate(Sum('amount'))

    sum_of_expenses_amount = sum_of_expenses['amount__sum'] if sum_of_expenses['amount__sum'] else 0
    sum_of_income_amount = sum_of_income['amount__sum'] if sum_of_income['amount__sum'] else 0
    available_balance = sum_of_income_amount - sum_of_expenses_amount

    total_budget = TotalBudget.objects.filter(owner=user, month=current_month).first()

    total_budget_income = 0
    total_budget_expense = 0
    total_budget_balance = 0

    if total_budget:
        total_budget_income = total_budget.total_budget_income
        total_budget_expense = total_budget.total_budget_expense
        total_budget_balance = total_budget.total


    datetime_object = datetime.strptime(str(current_month), "%m")
    month_name = datetime_object.strftime("%b")
    full_month_name = datetime_object.strftime("%B")

    context={
            "all_expense":all_expense_serialized.data,
            "total_expense":sum_of_expenses_amount,
            "all_income":all_income_serialized.data,
            "total_income":sum_of_income_amount,
            "available_balance":available_balance,
            "month":month_name,
            "full_month_name":full_month_name,
            "budget_income":total_budget_income,
            "budget_expenses":total_budget_expense,
            "budget_balance":total_budget_balance,
            "currency":currency
        }
    EmailServices.send_async(
        template="report.html",
        subject=f"Fintrak {full_month_name} Report",
        recipients=[user.email],
        context=context
    )
