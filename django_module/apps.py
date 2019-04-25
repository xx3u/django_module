from django.apps import AppConfig


class DjangoModuleConfig(AppConfig):
    name = 'django_module'

    def ready(self, *args, **kwargs):
        import django_module.signals
