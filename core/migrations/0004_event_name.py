# Generated by Django 4.2.2 on 2024-02-23 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_customer_address_city_customer_address_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]
