# Generated by Django 3.0.8 on 2020-07-31 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0004_auto_20200731_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
