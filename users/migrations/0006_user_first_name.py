# Generated by Django 3.2.8 on 2022-03-16 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220316_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
