# Generated by Django 3.0.4 on 2021-06-11 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendors', '0002_auto_20210611_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='bill_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateField(null=True),
        ),
    ]
