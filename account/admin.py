from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile
from django.utils.html import mark_safe
from django.urls import reverse
from social_django.models import Association, Nonce, UserSocialAuth


admin.site.unregister(Association)
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'پروفایل کاربران'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('display_profile_picture', 'full_name_link', 'username', 'get_phone_number', 'email')
    ordering = ('-date_joined',)


    def full_name_link(self, obj):
        full_name = f"{obj.first_name} {obj.last_name}"
        edit_url = reverse('admin:auth_user_change', args=[obj.id])  # لینک به صفحه ویرایش کاربر
        return mark_safe(f'<a href="{edit_url}">{full_name}</a>')

    full_name_link.short_description = 'نام کامل'

    def get_phone_number(self, obj):
        return obj.userprofile.phone_number if obj.userprofile else 'ندارد'

    get_phone_number.short_description = 'شماره تلفن'

    def display_profile_picture(self, obj):
        if hasattr(obj, 'userprofile') and obj.userprofile.profile_picture:
            return mark_safe(f'<img src="{obj.userprofile.profile_picture}" width="50" height="50" />')
        else:
            return mark_safe('<img src="/media/account/no-picture.png" width="50" height="50" />')

    display_profile_picture.short_description = 'تصویر پروفایل'


User._meta.verbose_name = 'کاربر'
User._meta.verbose_name_plural = 'کاربران'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
