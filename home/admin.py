from django.contrib import admin
from .models import HomePage

class HomePageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('بخش درباره ما', {
            'fields': ('aboutus_title', 'aboutus_text')
        }),
        ('بخش‌های محتوایی', {
            'fields': ('title_1', 'content_1', 'title_2', 'content_2', 'title_3', 'content_3')
        }),
        (None, {
            'fields': ('title_4', 'content_4')
        }),
        ('بخش اطلاعات تماس', {
            'fields': ('address_section', 'time_section', 'phone_section')
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(HomePage, HomePageAdmin)
