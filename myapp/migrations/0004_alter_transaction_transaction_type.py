# Generated by Django 4.1.3 on 2022-11-15 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_expense_name_transaction_transaction_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('Negative', 'Negative'), ('Positive', 'Positive')], default='Positive', max_length=50),
        ),
    ]
