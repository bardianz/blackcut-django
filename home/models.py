from django.db import models


class HomePage(models.Model):
    aboutus_title = models.CharField(verbose_name="عنوان درباره ما", blank=False, max_length=40,default="پیش فرض")
    aboutus_text = models.TextField(verbose_name="متن درباره ما", blank=False)
    title_1 = models.CharField(verbose_name="عنوان 1", max_length=25, blank=False)
    content_1 = models.TextField(verbose_name="محتوا 1", blank=False)
    title_2 = models.CharField(verbose_name="عنوان 2", max_length=25, blank=False)
    content_2 = models.TextField(verbose_name="محتوا 2", blank=False)
    title_3 = models.CharField(verbose_name="عنوان 3", max_length=25, blank=False)
    content_3 = models.TextField(verbose_name="محتوا 3", blank=False)

    title_4 = models.CharField(verbose_name="عنوان 4", max_length=35, blank=False,default="")

    address_section = models.TextField(verbose_name="آدرس", blank=False)
    time_section = models.TextField(verbose_name="تایم کاری", blank=False)
    phone_section = models.TextField(verbose_name="شماره تلفن", blank=False)

    class Meta:
        verbose_name = "محتوا"
        verbose_name_plural = "محتواها"

    def __str__(self) -> str:
        return "محتوا"
