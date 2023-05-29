# Generated by Django 4.0.6 on 2023-01-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youpayclient', '0003_youpayclienttransactiondata_available_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='cancel_url',
            field=models.CharField(blank=True, help_text='Cancel URL, example :http://www.example.com/cancel/', max_length=500),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='cart_VAT_amount',
            field=models.DecimalField(blank=True, decimal_places=4, help_text='used to store cart VAT amount', max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='cart_amount',
            field=models.DecimalField(blank=True, decimal_places=4, help_text='used to store cart VAT amount', max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='cart_base_amount',
            field=models.DecimalField(blank=True, decimal_places=4, help_text='used to store cart base amount', max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='cart_currency',
            field=models.CharField(blank=True, help_text='used to store cart currency details', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='cart_service_fee',
            field=models.DecimalField(blank=True, decimal_places=4, help_text='used to store cart service fee', max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='customer_name',
            field=models.CharField(blank=True, help_text='To store name', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='failure_url',
            field=models.CharField(blank=True, help_text='Failure URL, example :http://www.example.com/failure/', max_length=500),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='language',
            field=models.CharField(blank=True, help_text='to identify the language', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='loyalty_level',
            field=models.IntegerField(blank=True, default=0, help_text='used to store loyalty level', null=True),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='name_on_card',
            field=models.CharField(blank=True, help_text='Denotes the name on the card', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='order_history',
            field=models.JSONField(blank=True, help_text='used to store order history', null=True),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='order_items',
            field=models.JSONField(blank=True, help_text='used to store order history', null=True),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='session_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='success_url',
            field=models.CharField(blank=True, help_text='Success URL, example :http://www.example.com/success/', max_length=500),
        ),
        migrations.AddField(
            model_name='youpayclienttransactiondata',
            name='verify_url',
            field=models.CharField(blank=True, help_text='Verify URL, example :http://www.example.com/verify/', max_length=500),
        ),
    ]