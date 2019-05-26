from django.apps import AppConfig


class QuestionaryConfig(AppConfig):
    name = 'questionary'

    def ready(self):
        super().ready()
        from questionary import signal_handlers
