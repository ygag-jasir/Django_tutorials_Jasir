from django.contrib import admin
from youpayclient.models import YouPayClientTransactionData


class YouPayClientTransactionDataAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'payment_reference', 'invoice_id',
                    'amount', 'currency', 'customer_email', 'payment_gateway',
                    'approved', 'payment_status', 'created_on', 'modified_on')
    search_fields = ('transaction_id', 'invoice_id', 'customer_email',)
    list_filter = ('settlement_entity', 'payment_status', 'approved',
                   'payment_gateway', 'currency','created_on')

        
    # disable add , edit and delete functionality
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(YouPayClientTransactionData,
                    YouPayClientTransactionDataAdmin)
