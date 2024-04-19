from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
     empty_value_display = "-هیچ آیتمی وجود ندارد-"

admin.site.register(Product,ProductAdmin)
