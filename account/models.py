
from django.contrib.auth.models import AbstractUser ,Group, Permission
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError(
            _('شماره تلفن فقط باید شامل اعداد باشد.')
        )
    if len(value) != 11:
        raise ValidationError(
            _('شماره تلفن باید 11 رقم باشد.')
        )
class CustomUser(AbstractUser):
    profile_picture = models.URLField(max_length=500, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True, validators=[validate_phone_number])
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # اضافه کردن related_name برای جلوگیری از تداخل
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_user_permissions',  # اضافه کردن related_name برای جلوگیری از تداخل
        blank=True
    )
