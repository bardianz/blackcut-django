from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy
from jalali_date import date2jalali

from shop.models import Product
from utils.persian_date_convertor import persian_date_string_convertor
from utils.persian_weekday import convert_to_persian_weekday

from PIL import Image


SERVICE_IS_ACTIVE_CHOICES = (
    (True, gettext_lazy("فعال")),
    (False, gettext_lazy("غیرفعال")),
)


class Service(models.Model):
    class Meta:
        verbose_name = "سرویس"
        verbose_name_plural = "سرویس‌ها"

    service_name = models.CharField(verbose_name="نام سرویس", max_length=15)
    img = models.ImageField(default="reservation//no-picture.png", upload_to='reservation/service/images/', verbose_name="تصویر سرویس")
    desc = models.CharField(verbose_name="توضیحات سرویس", max_length=80,blank = True,null=True)
    is_active = models.BooleanField(verbose_name="وضعیت فعال بودن", choices=SERVICE_IS_ACTIVE_CHOICES,
                                    default=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.img.path)
        # img.thumbnail((100, 100))
        img.save(self.img.path)

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
    date = models.DateField(verbose_name="تارخ")
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="بازه زمانی")
    is_active = models.BooleanField(verbose_name="آیا این نوبت فعال است", default=True, blank=True, null=True)
    is_done = models.BooleanField(verbose_name="آیا انجام شده است", default=False, blank=True, null=True)
    is_paid = models.BooleanField(verbose_name="آیا پرداخت شده است", default=False, blank=True, null=True)
    is_canceled = models.BooleanField(verbose_name="آیا نوبت لغو شده است؟", default=False, blank=True, null=True)
    is_expired = models.BooleanField(verbose_name="آیا نوبت منقضی شده است؟", default=False, blank=True, null=True)
    products = models.ManyToManyField(Product,blank=True,verbose_name="محصولات انتخابی")

    STATUS_CHOICES = [
    ("active", "فعال"),
    ("canceled", "لغو شده"),
    ("expired", "منقضی"),
    ("done", "انجام شده"),
    ("paid", "پرداخت شده"),
]
    status = models.CharField(choices=STATUS_CHOICES , max_length=25,default="active",verbose_name="وضعیت")


    def save(self, *args, **kwargs):




        if self.is_canceled:
            self.is_done = False
            self.is_active = False
            self.is_paid = False
            self.is_expired = True

        if self.is_done:
            self.is_active = False

        if self.is_paid:
            self.is_active = False
            self.is_done = True


        super().save(*args, **kwargs)

    def jalali_reservation_date(self):
        jalali_date = date2jalali(self.date)
        jalali_string = persian_date_string_convertor(str(jalali_date))
        persian_weekday = convert_to_persian_weekday(self.date)
        return f"{persian_weekday} {jalali_string}"

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
            return "Unknown"

    def __str__(self):
        return f"{self.user_identifier()}  | {self.jalali_reservation_date()}  |  {self.timeslot}"
