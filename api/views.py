from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from reservation.models import Appointment
from shop.models import Product
from .serializers import AppointmentSerializer,ProductsSerializer


class ActiveAppointments(APIView):
    def get_queryset(self):
        return Appointment.objects.filter(is_active=True).order_by('date', 'timeslot__start_time')

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


class AddProductToAppointment(APIView):
    def post(self, request):
        appointment_id = request.data.get('appointment_id')
        product_id = request.data.get('product_id')
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            product = Product.objects.get(id=product_id)
            appointment.products.add(product)
            appointment.save()
            return Response({'message': 'Product added successfully'}, status=status.HTTP_200_OK)
        except Appointment.DoesNotExist:
            return Response({'message': 'Appointment does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Product.DoesNotExist:
            return Response({'message': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def remove_product_from_appointment(request):
    appointment_id = request.data.get('appointment_id')
    product_id = request.data.get('product_id')
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        product = Product.objects.get(id=product_id)
        appointment.products.remove(product)
        appointment.save()
        return Response({'message': 'Product removed successfully'},status=status.HTTP_200_OK)
    except Appointment.DoesNotExist:
        return Response({'message': 'Appointment does not exist'},status=status.HTTP_404_NOT_FOUND)
    except Product.DoesNotExist:
        return Response({'message': 'Product does not exist'},status=status.HTTP_404_NOT_FOUND)