# Generated by Django 4.0.6 on 2022-10-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YouPayClientTransactionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_reference', models.CharField(blank=True, max_length=200, null=True)),
                ('order_reference', models.CharField(blank=True, max_length=200, null=True)),
                ('invoice_id', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=12)),
                ('currency', models.CharField(blank=True, max_length=5, null=True)),
                ('service_fee', models.DecimalField(decimal_places=4, max_digits=12)),
                ('base_amount', models.DecimalField(decimal_places=4, max_digits=12)),
                ('vat_amount', models.DecimalField(decimal_places=4, max_digits=12)),
                ('customer_ip_address', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_email', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_gateway', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('channel_code', models.CharField(blank=True, help_text='Channel code used for the transaction, if transaction is through checkout', max_length=120, null=True)),
                ('is_fraud', models.BooleanField(default=False, help_text='Denotes whether the payment is fraud or not.')),
                ('is_flagged', models.BooleanField(default=False, help_text='Denotes whether the payment is marked as flagged or not.')),
                ('card_bin', models.CharField(blank=True, help_text='Denotes the bin number of the card used for the payment', max_length=6, null=True)),
                ('card_last4', models.CharField(blank=True, help_text='Denotes the last 4 digits of the card used for the payment', max_length=4, null=True)),
                ('payment_method', models.CharField(blank=True, help_text='Payment Method', max_length=200, null=True)),
                ('payment_scheme', models.CharField(blank=True, help_text='Denotes the payment scheme used for the payment', max_length=200, null=True)),
                ('is_gcc_card', models.BooleanField(default=False, help_text='Determine whether the transaction is carried out using card belongs to GCC country.')),
                ('card_issuer_country', models.CharField(blank=True, db_index=True, help_text='Denotes two letter code of card issued country.', max_length=4, null=True)),
                ('platform', models.CharField(blank=True, help_text='to identify the platform', max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
