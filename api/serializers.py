from rest_framework import serializers
from reservation.models import Appointment
from shop.models import Category, Product


class AppointmentSerializer(serializers.ModelSerializer):
    jalali_reservation_date = serializers.CharField(read_only=True)
    user_identifier = serializers.CharField(read_only=True)
    start_time = serializers.TimeField(source='timeslot.start_time', read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'user', 'service', 'date', 'start_time', 'timeslot', 'is_active', 'is_done', 'is_paid',
                  'is_canceled', 'jalali_reservation_date', 'user_identifier', 'products','status']
        ordering = ['date', 'start_time']

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
