# Generated by Django 3.0.4 on 2020-06-08 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceManagement', '0003_auto_20200608_0800'),
        ('projectManagement', '0004_auto_20200423_1920'),
        ('accountManagement', '0002_auto_20200608_0800'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='projectExpense',
            new_name='generalExpense',
        ),
        migrations.AddField(
            model_name='operatingexpense',
            name='project',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='projectO', to='projectManagement.project'),
            preserve_default=False,
        ),
    ]