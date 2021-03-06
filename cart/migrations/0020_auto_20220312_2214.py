# Generated by Django 3.2.8 on 2022-03-12 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('cart', '0019_auto_20220312_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='content_type',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
