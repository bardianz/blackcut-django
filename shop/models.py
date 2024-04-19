from django.db import models
from django.conf import settings
from pathlib import Path

BASE_DIR = Path(settings.BASE_DIR)

class Product(models.Model):
    name = models.CharField(max_length=50,verbose_name="تصویر محصول")
    img = models.ImageField(default=str(BASE_DIR / "static" / "shop" / "no-picture.png") ,upload_to='shop/product/images/', verbose_name="تصویر محصول")
    quantity = models.IntegerField(default=0 ,verbose_name="تصویر محصول")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self) -> str:
        return self.name