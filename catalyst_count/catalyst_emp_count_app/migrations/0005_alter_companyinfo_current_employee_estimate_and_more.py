# Generated by Django 4.2.15 on 2024-08-31 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst_emp_count_app', '0004_alter_companyinfo_current_employee_estimate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='current_employee_estimate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='total_employee_estimate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
