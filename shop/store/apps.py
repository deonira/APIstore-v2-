from django.apps import AppConfig
class StoreConfig(AppConfig):
    name = 'store'

    def ready(self):
        import store.signals

class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'
