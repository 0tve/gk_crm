# Generated by Django 4.2.1 on 2023-06-22 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0013_lead_active_alter_lead_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='active',
            new_name='is_active',
        ),
    ]
