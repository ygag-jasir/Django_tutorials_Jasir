# Generated by Django 4.0.6 on 2023-11-01 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youpayclient', '0011_alter_youpayclienttransactiondata_is_qitaf_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='brand_calculations',
            field=models.JSONField(blank=True, help_text='Calculated brand details', null=True),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='brand_details',
            field=models.JSONField(blank=True, help_text='used to store brand details from the API client', null=True),
        ),
    ]
