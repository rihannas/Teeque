# Generated by Django 4.2.15 on 2024-09-03 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teequeapp', '0010_rename_service_id_orderitem_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
    ]
