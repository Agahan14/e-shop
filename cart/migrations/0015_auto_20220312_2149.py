# Generated by Django 3.2.8 on 2022-03-12 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220312_2133'),
        ('cart', '0014_auto_20220312_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='price',
            new_name='total_price',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]