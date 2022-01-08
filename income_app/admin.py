from django.contrib import admin

from .models import Income


class IncomeAdmin(admin.ModelAdmin):
    model = Income
    list_display=('owner', 'amount', 'source', 'income_date')
    

admin.site.register(Income, IncomeAdmin)