# Generated by Django 3.0.8 on 2020-07-31 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0002_auto_20200719_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='type_order',
            field=models.CharField(choices=[('Expense', 'EXPENSE'), ('Revenue', 'REVENUE')], default='EXPENSE', max_length=7),
        ),
    ]
