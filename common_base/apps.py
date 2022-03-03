from django.apps import AppConfig


class CommonBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'common_base'
