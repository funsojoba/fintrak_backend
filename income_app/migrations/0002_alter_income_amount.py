# Generated by Django 3.2.6 on 2021-08-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
