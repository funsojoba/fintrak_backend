# Generated by Django 3.2.6 on 2021-08-20 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('phone', models.CharField(blank=True, max_length=256, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('prefered_currency', models.CharField(default='USD - $', max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]