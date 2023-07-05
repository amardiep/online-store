# Generated by Django 4.1.3 on 2023-03-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
                ('oid', models.CharField(blank=True, max_length=150)),
                ('amountpaid', models.CharField(blank=True, max_length=500, null=True)),
                ('paymentstatus', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=500)),
                ('delivered', models.BooleanField(default=False)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=5000),
        ),
    ]