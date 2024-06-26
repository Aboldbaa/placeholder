# Generated by Django 5.0.2 on 2024-03-23 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_invoice_ship_to_address_invoice_ship_to_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='bill_to_city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='bill_to_state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='bill_to_zip',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
