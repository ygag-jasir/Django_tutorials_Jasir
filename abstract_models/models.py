from django.db import models

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

class ModelA(Base):
    """
    Model A
    """
    level = models.IntegerField(null=False,blank=False)