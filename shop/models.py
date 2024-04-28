from django.db import models
from PIL import Image

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام محصول")
    img = models.ImageField(default="shop/no-picture.png", upload_to='shop/product/images/', verbose_name="تصویر محصول")
    quantity = models.IntegerField(default=0, verbose_name="موجودی محصول")
    price = models.IntegerField(verbose_name='قیمت به تومان')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.img.path)
        img.thumbnail((100, 100))
        img.save(self.img.path)

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self) -> str:
        return self.name
