from rest_framework import serializers
from reservation.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    jalali_reservation_date = serializers.CharField(read_only=True)
    user_identifier = serializers.CharField(read_only=True)
    start_time = serializers.TimeField(source='timeslot.start_time', read_only=True)

    class Meta:
        model = Appointment
        fields = ['id','user', 'service', 'date', 'start_time', 'timeslot', 'is_active', 'is_done', 'is_paid', 'is_canceled', 'jalali_reservation_date', 'user_identifier']
