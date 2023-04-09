# Generated by Django 4.1.5 on 2023-02-26 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_product_color_product_size_alter_product_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('addressline1', models.TextField(blank=True, default='', null=True)),
                ('addressline2', models.TextField(blank=True, default='', null=True)),
                ('addressline3', models.TextField(blank=True, default='', null=True)),
                ('pin', models.TextField(blank=True, default='', null=True)),
                ('city', models.TextField(blank=True, default='', null=True)),
                ('state', models.TextField(blank=True, default='', null=True)),
                ('pic', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/buyers')),
            ],
        ),
    ]
