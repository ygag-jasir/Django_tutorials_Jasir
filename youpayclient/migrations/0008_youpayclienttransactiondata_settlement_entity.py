# Generated by Django 4.0.6 on 2023-04-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youpayclient', '0007_youpayclienttransactiondata_gateway_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='settlement_entity',
            field=models.CharField(blank=True, help_text='used to store settlement entity', max_length=100, null=True),
        ),
    ]
