# Generated by Django 3.0.8 on 2020-07-31 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0003_auto_20200731_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='type_order',
            field=models.CharField(choices=[('expense', 'EXPENSE'), ('revenue', 'REVENUE')], default='EXPENSE', max_length=7),
        ),
    ]
