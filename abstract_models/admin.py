from django.contrib import admin

from abstract_models.models import ModelA

# Register your models here.

class ModelAAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level',)

admin.site.register(ModelA,ModelAAdmin)