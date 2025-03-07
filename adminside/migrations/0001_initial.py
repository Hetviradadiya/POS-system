# Generated by Django 5.1.6 on 2025-03-07 07:02

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_location', models.CharField(max_length=50)),
                ('branch_area', models.CharField(max_length=50)),
                ('branch_phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('branch_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('categories_id', models.AutoField(primary_key=True, serialize=False)),
                ('categories_name', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_firstname', models.CharField(max_length=50)),
                ('customer_lastname', models.CharField(max_length=50)),
                ('customer_email', models.EmailField(blank=True, max_length=20)),
                ('customer_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('food_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('food_item_name', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=100)),
                ('quantity', models.IntegerField(null=True)),
                ('branch', models.CharField(max_length=20)),
                ('sell_price', models.IntegerField()),
                ('cost_price', models.IntegerField()),
                ('mfg_date', models.DateField()),
                ('exp_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('food_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('food_item', models.CharField(max_length=50)),
                ('cost_price', models.IntegerField()),
                ('supplier_id', models.IntegerField()),
                ('purchased_date', models.DateField()),
                ('payment_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sales_reports',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('categories', models.CharField(max_length=50)),
                ('quantities', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('supplier_email', models.EmailField(max_length=254)),
                ('supplier_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(max_length=250)),
                ('branch', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('table_id', models.AutoField(primary_key=True, serialize=False)),
                ('seats', models.IntegerField()),
                ('status', models.CharField(choices=[('vacant', 'Vacant'), ('reserved', 'Reserved'), ('occupied', 'Occupied')], default='vacant', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_username', models.CharField(max_length=50, unique=True)),
                ('staff_fullname', models.CharField(max_length=100)),
                ('staff_email', models.EmailField(max_length=50, unique=True)),
                ('staff_password', models.CharField(max_length=128)),
                ('staff_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('staff_img', models.ImageField(blank=True, null=True, upload_to='staff_images/')),
                ('staff_role', models.CharField(choices=[('Manager', 'Manager'), ('Employee', 'Employee')], max_length=50)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff_members', to='adminside.branch')),
            ],
        ),
    ]
