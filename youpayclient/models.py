from django.db import models


class AbstractDateTime(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class YouPayClientTransactionData(AbstractDateTime):
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    payment_reference = models.CharField(
        max_length=200, null=True, blank=True)
    order_reference = models.CharField(
        max_length=200, null=True, blank=True)
    invoice_id = models.CharField(
        max_length=100, null=True, blank=True)

    amount = models.DecimalField(decimal_places=4, max_digits=12)
    currency = models.CharField(max_length=5, null=True, blank=True)
    service_fee = models.DecimalField(decimal_places=4, max_digits=12, 
                                      null=True, blank=True)
    base_amount = models.DecimalField(decimal_places=4, max_digits=12, 
                                      null=True, blank=True)
    vat_amount = models.DecimalField(decimal_places=4, max_digits=12, 
                                     null=True, blank=True)

    customer_ip_address = models.CharField(
        max_length=100, null=True, blank=True)
    customer_email = models.CharField(max_length=200, null=True, blank=True)
    customer_name = models.CharField(max_length=100, null=True, blank=True,
                                     help_text="To store name")
    payment_gateway = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.CharField(max_length=100, null=True, blank=True)

    channel_code = models.CharField(
        max_length=120, null=True, blank=True,
        help_text="Channel code used for the transaction, if transaction is"
                  " through checkout")
    is_fraud = models.BooleanField(
        default=False,
        help_text='Denotes whether the payment is fraud or not.')
    is_flagged = models.BooleanField(
        default=False,
        help_text='Denotes whether the payment is marked as flagged or not.')
    card_bin = models.CharField(
        max_length=6, null=True, blank=True,
        help_text='Denotes the bin number of the card used for the payment')
    card_last4 = models.CharField(
        max_length=4, null=True, blank=True,
        help_text='Denotes the last 4 digits of the '
                  'card used for the payment')
    payment_method = models.CharField(
        max_length=200,  null=True, blank=True, help_text='Payment Method')
    payment_scheme = models.CharField(
        max_length=200, null=True, blank=True,
        help_text='Denotes the payment scheme used for the payment')
    is_gcc_card = models.BooleanField(
        default=False,
        help_text='Determine whether the transaction is carried out using '
                  'card belongs to GCC country.')
    card_issuer_country = models.CharField(
        max_length=4, null=True, blank=True, db_index=True,
        help_text='Denotes two letter code of card issued country.')
    platform = models.CharField(
        max_length=200, null=True, blank=True,
        help_text="to identify the platform")
    response_summary = models.CharField(
        max_length=500, null=True, blank=True,
        help_text='Checkout response summary text')
    approved = models.BooleanField(
        default=False,
        help_text='Denotes whether the payment is approved or not')

    # adcb related data
    redeemed_amount = models.DecimalField(
        decimal_places=4, max_digits=12, null=True, blank=True,
        help_text='amount which was redeemed on ADCB')
    redeemed_points = models.DecimalField(
        decimal_places=4, max_digits=12, null=True, blank=True,
        help_text='points which was redeemed on ADCB')
    payable_amount = models.DecimalField(
        decimal_places=4, max_digits=12, null=True, blank=True,
        help_text='amount which is paid using '
                  'credit/debit card by the customer')
    available_amount = models.DecimalField(
        decimal_places=4, max_digits=12, null=True, blank=True,
        help_text='Available amount for the card')
    available_points = models.DecimalField(
        decimal_places=4, max_digits=12, null=True, blank=True,
        help_text='Available points for the card')
    is_full_redemption = models.BooleanField(
        db_index=True, null=True, blank=True,
        help_text='Denotes whether the redemption is full or not.')

    order_history = models.JSONField(null=True, blank=True,
                                     help_text="used to store order history")
    session_id = models.CharField(max_length=500, null=True, blank=True)
    name_on_card = models.CharField(max_length=255, null=True, blank=True,
                                    help_text='Denotes the name on the card')
    success_url = models.CharField(
        max_length=500, blank=True,
        help_text='Success URL, example :http://www.example.com/success/')
    failure_url = models.CharField(
        max_length=500, blank=True,
        help_text='Failure URL, example :http://www.example.com/failure/')
    cancel_url = models.CharField(
        max_length=500, blank=True,
        help_text='Cancel URL, example :http://www.example.com/cancel/')
    verify_url = models.CharField(
        max_length=500, blank=True,
        help_text='Verify URL, example :http://www.example.com/verify/')

    language = models.CharField(max_length=15, null=True, blank=True,
                                help_text="to identify the language")
    order_items = models.JSONField(null=True, blank=True,
                                   help_text="used to store order history")
    loyalty_level = models.IntegerField(
        null=True, blank=True, default=0,
        help_text="used to store loyalty level")
    cart_amount = models.DecimalField(decimal_places=4, max_digits=12,
                                      null=True, blank=True,
                                      help_text="used to store cart "
                                                "VAT amount")
    cart_currency = models.CharField(null=True, blank=True, max_length=15,
                                     help_text="used to store cart currency "
                                               "details")
    cart_service_fee = models.DecimalField(decimal_places=4, max_digits=12,
                                           null=True, blank=True,
                                           help_text="used to store cart "
                                                     "service fee")
    cart_base_amount = models.DecimalField(decimal_places=4, max_digits=12,
                                           null=True, blank=True,
                                           help_text="used to store cart "
                                                     "base amount")
    cart_VAT_amount = models.DecimalField(decimal_places=4, max_digits=12,
                                          null=True, blank=True,
                                          help_text="used to store cart "
                                                    "VAT amount")
    processing_fee = models.DecimalField(decimal_places=4, max_digits=12,
                                         null=True, blank=True,
                                         help_text="used to store gateway "
                                                   "processing fee")
    paid_amount = models.DecimalField(decimal_places=4, max_digits=12,
                                      null=True, blank=True,
                                      help_text="used to store gateway total amount paid by customer")
    gateway_charge = models.DecimalField(
        decimal_places=4, max_digits=12, null=True, blank=True,
        help_text="Used to store calculated gateway charges "
                  "based on the configuration")
    settlement_entity = models.CharField(
        max_length=100, null=True, blank=True,
        help_text="used to store settlement entity")
    is_qitaf_enabled = models.BooleanField(null=True, blank=True,
                                           default=False, db_index=True,)
    qitaf_request_id = models.CharField(max_length=100, null=True,
                                        blank=True, db_index=True,
                                        help_text='Request id generated by Qitaf')
    earned_point = models.DecimalField(
        decimal_places=4, max_digits=12, null=True, blank=True,
        help_text='Earned point for the transaction via corresponding payment'
                  ' method')
    brand_details = models.JSONField(null=True, blank=True,
                                     help_text="used to store brand details "
                                               "from the API client")
    brand_calculations = models.JSONField(null=True, blank=True,
                                          help_text="Calculated brand details")
    

    def __str__(self):
        return str(self.transaction_id)
