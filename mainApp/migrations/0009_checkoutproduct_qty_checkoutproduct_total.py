# Generated by Django 4.1.7 on 2023-03-26 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutproduct',
            name='qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='checkoutproduct',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]