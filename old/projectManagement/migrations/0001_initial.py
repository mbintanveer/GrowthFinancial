# Generated by Django 3.0.4 on 2020-04-23 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='target',
            fields=[
                ('targetID', models.AutoField(primary_key=True, serialize=False)),
                ('targetDesc', models.TextField()),
                ('targetStatus', models.TextField()),
            ],
        ),
    ]