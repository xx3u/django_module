# Generated by Django 2.2 on 2019-04-07 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_module', '0002_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='Product',
            new_name='product',
        ),
    ]
