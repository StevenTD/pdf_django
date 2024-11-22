from django.apps import AppConfig


class PdfDjangoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pdf_django_app'

    def ready(self):
        import pdf_django_app.signals
