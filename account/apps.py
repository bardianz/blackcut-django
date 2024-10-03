from django.apps import AppConfig
from django.contrib.auth.apps import AuthConfig
from django.utils.translation import gettext_lazy as _

class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
    verbose_name = 'حساب کاربری'



class CustomAuthConfig(AuthConfig):
    name = 'django.contrib.auth'
    verbose_name = _('مدیریت کاربرها')