from rest_framework import serializers
from reservation.models import Appointment
from shop.models import Category, Product

from django.conf import settings

class AppointmentSerializer(serializers.ModelSerializer):
    jalali_reservation_date = serializers.CharField(read_only=True)
    user_identifier = serializers.CharField(read_only=True)
    start_time = serializers.TimeField(source='timeslot.start_time', read_only=True)
    phone_number = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ['id', 'user', 'service', 'date', 'start_time', 'timeslot', 'is_active', 'is_done', 'is_paid',
                  'is_canceled', 'jalali_reservation_date', 'user_identifier', 'products','status','phone_number', 'profile_picture']
        ordering = ['date', 'start_time']

    def get_phone_number(self, obj):
        user_profile = getattr(obj.user, 'userprofile', None)  # استفاده از getattr برای دسترسی به UserProfile
        return user_profile.phone_number if user_profile else None

    def get_profile_picture(self, obj):
        request = self.context.get('request')
        user_profile = getattr(obj.user, 'userprofile', None)  # استفاده از getattr برای دسترسی به UserProfile
        # return user_profile.profile_picture if user_profile else f"{settings.STATIC_URL}/account/no-picture.png"
        if user_profile and user_profile.profile_picture:
            return user_profile
        else:
            return request.build_absolute_uri(f"{settings.STATIC_URL}account/no-picture.png")

class ProductsSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id","name", "img", "price", "quantity"]

    def get_price(self, obj):
        return format(obj.price, ',')



class CategorySerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['title', 'rank', 'products']
