# Generated by Django 3.2.8 on 2022-03-11 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_cartitem_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='total_price',
            new_name='price',
        ),
    ]
