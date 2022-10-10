# Generated by Django 4.1.1 on 2022-10-09 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maipogrande', '0005_alter_contact_id_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banks', to=settings.AUTH_USER_MODEL),
        ),
    ]