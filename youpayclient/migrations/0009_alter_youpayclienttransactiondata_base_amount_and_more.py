# Generated by Django 4.0.6 on 2023-05-23 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youpayclient', '0008_youpayclienttransactiondata_settlement_entity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youpayclienttransactiondata',
            name='base_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='youpayclienttransactiondata',
            name='service_fee',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='youpayclienttransactiondata',
            name='vat_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True),
        ),
    ]