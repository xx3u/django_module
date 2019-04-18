# Generated by Django 2.2 on 2019-04-14 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_module', '0007_auto_20190411_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='method',
            field=models.CharField(choices=[('card', 'card'), ('cash', 'cash'), ('qiwi', 'qiwi')], default='card', max_length=10),
        ),
    ]