from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy
from utils.jalali_weekday import jalali_weekday_convertor

SERVICE_IS_ACTIVE_CHOICES = (
    (True, gettext_lazy("فعال")),
    (False, gettext_lazy("غیرفعال")),
)


class Service(models.Model):
    class Meta:
        verbose_name = "سرویس"
        verbose_name_plural = "سرویس‌ها"

    service_name = models.CharField(verbose_name="نام سرویس", max_length=15)
    is_active = models.BooleanField(verbose_name="آی این خدمت قابل ارائه است؟", choices=SERVICE_IS_ACTIVE_CHOICES,
                                    default=True)

    def get_service_name(self):
        return self.service_name

    def __str__(self):
        return f"{self.service_name}"


class TimeSlot(models.Model):
    class Meta:
        verbose_name = "بازه زمانی"
        verbose_name_plural = "بازه های زمانی"

    start_time = models.TimeField(null=True, unique=True)
    finish_time = models.TimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.start_time)


class Appointment(models.Model):
    class Meta:
        verbose_name = "نوبت"
        verbose_name_plural = "نوبت‌ها"

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="کاربر")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True, verbose_name="سرویس")
    date = models.DateField(verbose_name="بازه زمانی")
    # start_time = models.TimeField(null=True)
    # finish_time = models.TimeField(null=True)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.DO_NOTHING, null=True, blank=True,
                                 verbose_name="بازه زمانی")
    is_active = models.BooleanField(verbose_name="آیا این نوبت فعال است", default=True, blank=True, null=True)
    is_done = models.BooleanField(verbose_name="آیا انجام شده است", default=False, blank=True, null=True)
    is_paid = models.BooleanField(verbose_name="آیا پرداخت شده است", default=False, blank=True, null=True)
    is_canceled = models.BooleanField(verbose_name="آیا نوبت لغو شده است؟", default=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.is_canceled:
            self.is_done = False
            self.is_active = False
            self.is_paid = False

        if self.is_done:
            self.is_active = False

        if self.is_paid:
            self.is_active = False
            self.is_done = True

        super().save(*args, **kwargs)

    def jalali_reservation_date(self):
        return jalali_weekday_convertor(self.date)

    def user_identifier(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        elif self.user.first_name:
            return f"{self.user.first_name}"
        elif self.user.email:
            return self.user.email
        elif self.user.username:
            return self.user.username
        else:
            return ""

    def __str__(self):
        return f"{self.user_identifier()}  | {self.jalali_reservation_date()}  |  {self.timeslot}"
