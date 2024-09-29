from django.db import models
from PIL import Image


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان دسته بندی")
    rank = models.IntegerField(verbose_name='رتبه قرارگیری',default=0,)

    @property
    def products(self):
        return Product.objects.filter(category=self)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام محصول")
    img = models.ImageField(default="reservation//no-picture.png", upload_to='shop/product/images/', verbose_name="تصویر محصول")
    price = models.IntegerField(verbose_name='قیمت به تومان',default=0,)
    quantity = models.IntegerField(verbose_name='تعداد',default=0  , null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None,null=True,blank=True)



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
