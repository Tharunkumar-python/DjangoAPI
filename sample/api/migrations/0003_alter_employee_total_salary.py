# Generated by Django 4.0.3 on 2022-12-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_employee_total_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='total_salary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
