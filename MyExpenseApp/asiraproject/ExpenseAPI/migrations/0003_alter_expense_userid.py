# Generated by Django 5.1.2 on 2024-10-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseAPI', '0002_alter_expense_createdat_alter_user_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='userID',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
