# Generated by Django 4.0.6 on 2022-10-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youpayclient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='approved',
            field=models.BooleanField(default=False, help_text='Denotes whether the payment is approved or not'),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='response_summary',
            field=models.CharField(blank=True, help_text='Checkout response summary text', max_length=500, null=True),
        ),
    ]
