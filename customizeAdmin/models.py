from django.db import models

# Create your models here.
class SampleWalletTransactions(models.Model):
    amount_in = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True, blank=True)
    amount_out = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True, blank=True)
    user = models.CharField(max_length=255)
        
    @property
    def remaining_balance(self):
        transaction_obj = SampleWalletTransactions.objects.filter(user=self.user)
        return remaning_balance(transaction_obj)

    def calculate_remaning(self):
        amt_in = self.amount_in if self.amount_in else 0
        amt_out = self.amount_out if self.amount_out else 0
        return amt_in - amt_out
        
    def display_remaining_balance(self):
        return self.calculate_remaning()
    

    
    display_remaining_balance.admin_order_field = 'remaining_balance' #Allows column order sorting
    display_remaining_balance.short_description = "Total" #Used in list_display for booleans
    
def remaning_balance(transaction_obj):
    if transaction_obj:
        amount_in = transaction_obj.aggregate(models.Sum('amount_in'))['amount_in__sum']
        amount_out = transaction_obj.aggregate(models.Sum('amount_out'))['amount_out__sum']
        return amount_in - amount_out
    else:
        return None
    