from django.contrib import admin
from .models import HomePage

class HomePageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(HomePage, HomePageAdmin)
