from django.contrib import admin
from .models import Service, TimeSlot, Appointment

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('service_name',)
    list_per_page = 20

class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'is_active')
    ordering = ('start_time',)
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('start_time', 'finish_time')
    list_per_page = 20

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user_identifier', 'service', 'jalali_reservation_date', 'timeslot', 'status')
    list_filter = ('status', 'service', 'date', )
    list_editable = ('status',)
    search_fields = ('user_identifier', 'jalali_reservation_date', 'user__first_name')
    list_per_page = 10

    def user_identifier(self, obj):
        return obj.user_identifier()

    user_identifier.short_description = "نام کاربر"

    def jalali_reservation_date(self, obj):
        return obj.jalali_reservation_date()

    jalali_reservation_date.short_description = "ناریخ"

admin.site.register(Service, ServiceAdmin)
admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Appointment, AppointmentAdmin)
