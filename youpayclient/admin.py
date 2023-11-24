from django.contrib import admin
from youpayclient.models import YouPayClientTransactionData


class YouPayClientTransactionDataAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'payment_reference', 'invoice_id',
                    'amount', 'currency', 'customer_email', 'payment_Gateway',
                    'approved', 'payment_status', 'created_on', 'modified_on')
    search_fields = ('transaction_id', 'invoice_id', 'customer_email',
                     'payment_reference', )
    list_filter = ('settlement_entity', 'payment_status', 'approved',
                   'payment_gateway', 'payment_method', 'currency','created_on',
                   'is_fraud', 'is_flagged', 'is_gcc_card', 
                   'is_full_redemption'
                   )
    
    fieldsets = (
        ('Customer details', {
            'fields': ('customer_name', 'customer_email', 'language',)
        }),
        ('Card details', {
            'fields': ('name_on_card', 'card_bin', 'card_last4',
                       'card_issuer_country', 'is_gcc_card',
                       )
        }),
        ('Order details', {
            'fields': ('invoice_id', 'order_reference', 'order_history',
                       'payment_status', 'approved', 'order_items',
                       )
        }),
        ('Cart details', {
            'fields': ('cart_amount', 'cart_currency', 'cart_service_fee',
                       'cart_base_amount', 'cart_VAT_amount', 'brand_details',
                       'brand_calculations'
                       )
        }),
        ('Payment details', {
            'fields': ('amount', 'currency', 
                       'transaction_id', 'payment_reference',
                       'settlement_entity', 'payment_gateway',
                       'channel_code', 'payment_method', 'payment_scheme',
                       'platform', 'response_summary', 'service_fee',
                       'base_amount', 'gateway_charge'
                       )
        }),
        ('URLs', {
            'fields': ('success_url', 'failure_url', 'cancel_url',
                       'verify_url',
                       )
        }),
        ('Risk details', {
            'fields': ('is_fraud', 'is_flagged',
                       )
        }),
        ('B2C Payback transaction details', {
            'fields': ('redeemed_amount', 'redeemed_points', 'payable_amount',
                       'available_amount', 'available_points',
                       'is_full_redemption',
                       )
        }),

        ('Quitaf transaction details', {
            'fields': ('is_qitaf_enabled',)
        }),
        ('Other Details', {
            'fields': ('session_id', 'loyalty_level', 'earned_point' )
        }),
    )
    
    # disable add , edit and delete functionality for client transaction data
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    

    def payment_Gateway(self, obj):
        
        if obj.payment_gateway:
            display_string = f"{obj.payment_gateway}"
            if obj.payment_method:
                display_string = f"{display_string} ({obj.payment_method})"
                
            return display_string
        else:
            return None


admin.site.register(YouPayClientTransactionData,
                    YouPayClientTransactionDataAdmin)
