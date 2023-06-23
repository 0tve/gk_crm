# Generated by Django 4.2.1 on 2023-06-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0012_alter_lead_age_alter_lead_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pictures/default-profile-pic.jpg', null=True, upload_to='profile_pictures/'),
        ),
    ]
