# Generated by Django 2.2 on 2019-04-25 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_module', '0005_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='django_module.City')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_cities', to='django_module.City')),
            ],
        ),
        migrations.RemoveField(
            model_name='store',
            name='product',
        ),
        migrations.RemoveField(
            model_name='store',
            name='quantity',
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='store',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='django_module.Location'),
        ),
        migrations.CreateModel(
            name='StoreItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('location', models.CharField(blank=True, max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_items', to='django_module.Product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='django_module.Store')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('method', models.CharField(choices=[('card', 'card'), ('cash', 'cash'), ('qiwi', 'qiwi')], default='card', max_length=10)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='django_module.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='django_module.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='django_module.Product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='django_module.Customer'),
        ),
    ]