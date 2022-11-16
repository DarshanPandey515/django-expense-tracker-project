# Generated by Django 4.1.3 on 2022-11-16 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='expense',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='income',
            field=models.FloatField(default=0),
        ),
    ]