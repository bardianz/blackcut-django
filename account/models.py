from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from django.contrib.auth.models import User


def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError(_('شماره تلفن فقط باید شامل اعداد باشد.'))
    if len(value) != 11:
        raise ValidationError(_('شماره تلفن باید 11 رقم باشد.'))


class UserProfile(models.Model):
    profile_picture = models.CharField(max_length=256,null=True, blank=True)
    # profile_picture = models.ImageField(upload_to='account/user-profile-picture/', blank=True, null=True,
    #                                     default="account/no-picture.png")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, blank=True, null=True, validators=[validate_phone_number])



    def __str__(self):
        return self.user.username
