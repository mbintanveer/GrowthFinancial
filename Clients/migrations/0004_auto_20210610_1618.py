# Generated by Django 3.0.4 on 2021-06-10 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0003_auto_20210610_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Clients.Client'),
        ),
    ]
