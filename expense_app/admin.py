from django.contrib import admin

from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    model = Expense
    list_display = ('owner', 'amount', 'category', 'expense_date')
    

admin.site.register(Expense, ExpenseAdmin)