from django.apps import AppConfig


class CustomizeadminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customizeAdmin'
