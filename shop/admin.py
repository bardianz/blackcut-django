from django.contrib import admin
from .models import Product,Category
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
     empty_value_display = "-هیچ آیتمی وجود ندارد-"

admin.site.register(Product,ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
     empty_value_display = "-هیچ دسته بندی‌ای وجود ندارد-"

admin.site.register(Category,CategoryAdmin)
