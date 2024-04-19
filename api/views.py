from rest_framework.views import APIView
from rest_framework.response import Response
from reservation.models import Appointment
from shop.models import Product
from .serializers import AppointmentSerializer


class ActiveAppointments(APIView):
    def get_queryset(self):
        return Appointment.objects.filter(is_active=True)

    def get(self, request):
        appointments = self.get_queryset()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)


class AllProducts(APIView):
    queryset = Product.objects.all()

    def get(self, request):
        products = self.queryset
        all_appointments = list(products.values())
        return Response(all_appointments)


