from rest_framework.views import APIView
from rest_framework.response import Response
from reservation.models import Appointment
from shop.models import Product
from .serializers import AppointmentSerializer,ProductsSerializer


class ActiveAppointments(APIView):
    def get_queryset(self):
        return Appointment.objects.filter(is_active=True)

    def get(self, request):
        appointments = self.get_queryset()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)


class AllProducts(APIView):
    def get_queryset(self):
        return Product.objects.all()

    def get(self, request):
        products = self.get_queryset()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

