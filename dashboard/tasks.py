from celery import shared_task
from datetime import datetime



def finance_report():
    current_month = datetime.now().month
    
    all_income = Income.objects.filter(
            owner=user, income_date__month=current_month).order_by('-created_at')
    
    all_expense = Expense.objects.filter(
            owner=user, expense_date__month=current_month).order_by('-created_at')
    


