# Generated by Django 3.2.8 on 2022-03-11 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_rename_price_cartitem_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
    ]
