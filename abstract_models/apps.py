from django.apps import AppConfig


class AbstractModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'abstract_models'
