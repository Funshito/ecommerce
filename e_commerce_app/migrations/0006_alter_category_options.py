# Generated by Django 5.1.1 on 2024-11-11 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0005_remove_order_product_remove_order_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]