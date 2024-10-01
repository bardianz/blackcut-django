from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile
from django.utils.html import mark_safe

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'پروفایل کاربران'

# ترکیب اطلاعات کاربر و پروفایل
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('display_profile_picture' , 'first_name', 'last_name','username', 'get_phone_number' ,'email', )

    def get_phone_number(self, obj):
        return obj.userprofile.phone_number if obj.userprofile else 'ندارد'

    get_phone_number.short_description = 'شماره تلفن'

    # نمایش تصویر پروفایل
    def display_profile_picture(self, obj):
        if hasattr(obj, 'userprofile') and obj.userprofile.profile_picture:
            return mark_safe(f'<img src="{obj.userprofile.profile_picture}" width="50" height="50" />')
        else:
            return mark_safe('<img src="/media/account/no-picture.png" width="50" height="50" />')

    display_profile_picture.short_description = 'تصویر پروفایل'

# حذف ثبت قبلی مدل User و ثبت مجدد با inline
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
