from django.db import models
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from django.db import transaction

# Create your models here.


class Base(models.Model):
    """
    Base class for all models
    """
    name = models.CharField(max_length=255,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        


@receiver(post_init, sender=Base)
def set_previous_name(sender, instance, **kwargs):
    instance.previous_name = instance.name


@receiver(post_save, sender=Base)
def update_client(sender, instance, created, **kwargs):
    """
    Signal to send webhook for client on each transaction
    """

    if instance.previous_name != instance.name:
        # logger for youpay status update
        print("Payment status updated for transaction ({}) : {} --> {}".format(instance.transaction_id,
                              instance.previous_name,
                              instance.name))


class ModelA(Base):
    """
    Model A
    """
    level = models.IntegerField(null=False,blank=False)
    
    
@receiver(post_init, sender=ModelA)
def set_previous_name(sender, instance, **kwargs):
    instance.previous_name = instance.name


@receiver(post_save, sender=ModelA)
def update_client(sender, instance, created, **kwargs):
    """
    Signal to send webhook for client on each transaction
    """

    if instance.previous_name != instance.name:
        # logger for youpay status update
        print("Payment status updated for transaction ({}) : {} --> {}"
                    "".format(instance.id,
                              instance.previous_name,
                              instance.name))
    
    a=1/0
    
    try:
        a=1/0
        raise DummyExcepction("123")

        transaction.on_commit(lambda: some_process)
        print("Transaciton commited")
    except Exception as e:
        print("Exc ",e)
        pass
class DummyExcepction(Exception):
    pass

def some_process():
    print("Someprocess STARTED")
    a=1/0
    raise DummyExcepction("123")
    
    print("Someprocess ENDED")
    
class TransactionData(models.Model):
    """
    TransactionData class for all models
    """
    name = models.CharField(max_length=255,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        


@receiver(post_init, sender=TransactionData)
def set_previous_name(sender, instance, **kwargs):
    instance.previous_name = instance.name


@receiver(post_save, sender=TransactionData)
def update_client(sender, instance, created, **kwargs):
    """
    Signal to send webhook for client on each transaction
    """

    if instance.previous_name != instance.name:
        # logger for youpay status update
        print("Payment status updated for transaction ({}) : {} --> {}"
                    "".format(instance.id,
                              instance.previous_name,
                              instance.name))