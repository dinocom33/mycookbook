from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.common'
    verbose_name = 'Common section'

    def ready(self):
        import apps.common.signals  # noqa
