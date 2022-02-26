from django.apps import AppConfig


class EventlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eventlog'
    def ready(self):
        import eventlog.signals
