from django.db import models
from ckeditor.fields import RichTextField


class HomePage(models.Model):
    aboutus_title = models.CharField(verbose_name="عنوان درباره ما", blank=False, max_length=40,default="پیش فرض")
    aboutus_text = RichTextField(verbose_name="متن درباره ما", blank=False,default="پیش فرض")
    title_1 = models.CharField(verbose_name="عنوان 1", max_length=25, blank=False,default="پیش فرض")
    content_1 = RichTextField(verbose_name="محتوا 1", blank=False,default="پیش فرض")
    title_2 = models.CharField(verbose_name="عنوان 2", max_length=25, blank=False,default="پیش فرض")
    content_2 = RichTextField(verbose_name="محتوا 2", blank=False,default="پیش فرض")
    title_3 = models.CharField(verbose_name="عنوان 3", max_length=25, blank=False,default="پیش فرض")
    content_3 = RichTextField(verbose_name="محتوا 3", blank=False,default="پیش فرض")

    title_4 = models.CharField(verbose_name="عنوان 4", max_length=35, blank=False,default="پیش فرض")
    content_4 = RichTextField(verbose_name="محتوا 4", blank=False,default="پیش فرض")

    address_section = RichTextField(verbose_name="آدرس", blank=False,default="پیش فرض")
    time_section = RichTextField(verbose_name="تایم کاری", blank=False,default="پیش فرض")
    phone_section = RichTextField(verbose_name="شماره تلفن", blank=False,default="پیش فرض")

    class Meta:
        verbose_name = "محتوا"
        verbose_name_plural = "محتوا"

    def __str__(self) -> str:
        return "برای تغییر محتوای صفحه اصلی کلیک کنید"
