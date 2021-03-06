# Generated by Django 3.1.3 on 2020-12-29 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_Login', '0001_initial'),
        ('App_Shop', '0002_product_added_to_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('added_time', models.DateTimeField(auto_now_add=True)),
                ('purchased', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='App_Login.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('cart_items', models.ManyToManyField(to='App_Order.Cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Login.customer')),
            ],
        ),
    ]
