# Generated by Django 4.2.1 on 2023-06-17 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0008_alter_lead_age_alter_lead_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='description',
        ),
        migrations.AddField(
            model_name='lead',
            name='address',
            field=models.TextField(default='addr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='order',
            field=models.TextField(default='ordr'),
            preserve_default=False,
        ),
    ]
