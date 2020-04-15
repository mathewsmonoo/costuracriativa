from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "itelie.users"
    verbose_name = _("User")
    verbose_name_plural = _("Users")

    def ready(self):
        try:
            import itelie.users.signals  # noqa F401
        except ImportError:
            pass
