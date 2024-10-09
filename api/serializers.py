from rest_framework import serializers
from reservation.models import Appointment
from shop.models import Category, Product

from django.conf import settings


class AppointmentSerializer(serializers.ModelSerializer):
    jalali_reservation_date = serializers.CharField(read_only=True)
    user_identifier = serializers.CharField(read_only=True)
    start_time = serializers.TimeField(source="timeslot.start_time", read_only=True)
    phone_number = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()
    is_done = serializers.SerializerMethodField()
    is_paid = serializers.SerializerMethodField()
    is_canceled = serializers.SerializerMethodField()
    is_expired = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = [
            "id",
            "user",
            "service",
            "date",
            "start_time",
            "timeslot",
            "jalali_reservation_date",
            "user_identifier",
            "products",
            "status",
            "phone_number",
            "profile_picture",
            "is_active",
            "is_done",
            "is_paid",
            "is_canceled",
            "is_expired",
        ]
        ordering = ["date", "start_time"]

    def get_is_active(self, obj):
        return obj.status == "active"

    def get_is_done(self, obj):
        return obj.status == "done"

    def get_is_paid(self, obj):
        return obj.status == "paid"

    def get_is_canceled(self, obj):
        return obj.status == "canceled"

    def get_is_expired(self, obj):
        return obj.status == "expired"

    def get_phone_number(self, obj):
        user_profile = getattr(
            obj.user, "userprofile", None
        )  # استفاده از getattr برای دسترسی به UserProfile
        return user_profile.phone_number if user_profile else None

    def get_profile_picture(self, obj):
        user_profile = getattr(
            obj.user, "userprofile", None
        )  # استفاده از getattr برای دسترسی به UserProfile
        return (
            user_profile.profile_picture
            if user_profile
            else "https://blackcut.pythonanywhere.com/static/account/no-picture.png"
        )


class ProductsSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "name", "img", "price", "quantity"]

    def get_price(self, obj):
        return format(obj.price, ",")


class CategorySerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["title", "rank", "products"]
