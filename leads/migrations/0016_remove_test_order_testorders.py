# Generated by Django 4.2.1 on 2023-06-23 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0015_order_alter_lead_category_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='order',
        ),
        migrations.CreateModel(
            name='TestOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_rel', to='leads.order')),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_rel', to='leads.test')),
            ],
        ),
    ]
