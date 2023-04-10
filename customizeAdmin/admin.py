from django import forms
from django.forms import ValidationError
from django.contrib import admin
from django.db.models import Sum

from customizeAdmin.models import SampleWalletTransactions

# Register your models here.


class SampleWalletTransactionsAdminForm(forms.ModelForm):
    class Meta:
        model = SampleWalletTransactions
        fields = '__all__'

    
    # validation for amount_out
    def clean_amount_out(self):
        amount_out = self.cleaned_data.get('amount_out')
        print("amount_out", amount_out)
        print("self.instance.remaining_balance", self.instance.remaining_balance)
        
        if self.instance.remaining_balance is not None:
            if amount_out > self.instance.remaining_balance:
                raise ValidationError("Amount out should be less than or equal to remaining balance")
            else:
                print("amount_out", amount_out)
            return amount_out
        return amount_out

    def clean_amount_in(self):
        print("Amount in validation")
        amount_in = self.cleaned_data.get('amount_in')
        print("amount_in", amount_in)
        if amount_in < 0:
            raise ValidationError("Amount in should be greater than 0")
        return amount_in
    
    
class SampleWalletTransactionsAdmin(admin.ModelAdmin):
    list_display = ('id','remaining_balance','amount_in', 'amount_out','total_amount_in', 'user','display_remaining_balance','my_function' )
    readonly_fields = ('remaining_balance',)
    list_filter = ('user',)
    
    form = SampleWalletTransactionsAdminForm
    
    # amount_in.description = 'Amount In **'
    
    
    def save_model(self, request, obj, form, change):
        
        super().save_model(request, obj, form, change)
    
    def my_function(self, obj) :
        """My Custom Title"""
        return "My Custom Value"
        
        
    my_function.short_description = 'This is the Column Name'
    
    def total_amount_in(self,obj):
        total_amount_in = SampleWalletTransactions.objects.aggregate(Sum('amount_in'))['amount_in__sum']
        return f'Total Amount In: ({total_amount_in})'

    total_amount_in.admin_order_field = 'amount_in' #Allows column order sorting
    total_amount_in.short_description = 'Total Amount In'

    
    
    # @admin.display(description='Sample details')
    # def sample(self, obj) :
    #     return 'Sample'


admin.site.register(SampleWalletTransactions,SampleWalletTransactionsAdmin)