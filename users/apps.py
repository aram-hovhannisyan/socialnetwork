from django.apps import AppConfig


class UsersConfig(AppConfig):
    'django.db.models.AutoField'
    name = 'users'

    def ready(self):
        import users.signals
