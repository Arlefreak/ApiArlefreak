from __future__ import unicode_literals
from django.apps import AppConfig


class LigojConfig(AppConfig):
    name = 'ligoj'
    def ready(self):
        import ligoj.signals
