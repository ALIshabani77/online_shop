# Generated by Django 5.0.7 on 2024-09-01 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_size_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
