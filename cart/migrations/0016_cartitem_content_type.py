# Generated by Django 3.2.8 on 2022-03-12 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('cart', '0015_auto_20220312_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='content_type',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
