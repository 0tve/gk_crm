# Generated by Django 4.2.1 on 2023-06-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0009_remove_lead_description_lead_address_lead_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='address',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='lead',
            name='order',
            field=models.CharField(),
        ),
    ]
