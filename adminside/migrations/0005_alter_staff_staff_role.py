# Generated by Django 5.1.6 on 2025-03-07 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0004_branch_branch_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staff_role',
            field=models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('staff', 'Staff')], max_length=50),
        ),
    ]
