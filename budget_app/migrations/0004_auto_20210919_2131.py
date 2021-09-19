# Generated by Django 3.2.6 on 2021-09-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0003_auto_20210906_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalbudget',
            name='total_budget_expense',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='totalbudget',
            name='total_budget_income',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
