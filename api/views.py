from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from reservation.models import Appointment
from shop.models import Category, Product
from .serializers import AppointmentSerializer, CategorySerializer,ProductsSerializer
from datetime import date
from rest_framework import generics


class ActiveAppointments(APIView):
    http_method_names = ['get',]
    def get_queryset(self):
        current_date = date.today()
        
        all_reservations = Appointment.objects.filter(status="active").order_by('date', 'timeslot__start_time')
        active_reservations= []
        for appointment in all_reservations:
            if appointment.status == "active":
                if appointment.date < current_date:
                    appointment.status="expired"
                    appointment.save()
                else:
                    active_reservations.append(appointment)

        return active_reservations
    
    def get(self, request):
        appointments = self.get_queryset()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)


class DoneAppointments(APIView):
    http_method_names = ['get', ]

    def get_queryset(self):
        return Appointment.objects.filter(status="done").order_by('date', 'timeslot__start_time')



    def get(self, request):
        appointments = self.get_queryset()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)


class AllAppointments(APIView):
    def get_queryset(self):
        current_date = date.today()
        all_reservations = Appointment.objects.exclude(status__in=["canceled", "expired"]).order_by('-date', 'timeslot__start_time')[:20]
        return all_reservations


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


class RemoveProductFromAppointment(APIView):
    def post(self, request):
        appointment_id = request.data.get('appointment_id')
        product_id = request.data.get('product_id')
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            product = Product.objects.get(id=product_id)
            appointment.products.remove(product)
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
    



    
class MakeDoneAppointment(APIView):
    def post(self, request):
        appointment_id = request.data.get('appointment_id')
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.is_done = True
            appointment.status = "done"
            appointment.save()
            return Response({'message': 'Product added successfully'}, status=status.HTTP_200_OK)
        except Appointment.DoesNotExist:
            return Response({'message': 'Appointment does not exist'}, status=status.HTTP_404_NOT_FOUND)


class MakePaidAppointment(APIView):
    def post(self, request):
        appointment_id = request.data.get('appointment_id')
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.is_paid = True
            appointment.status = "paid"
            appointment.save()
            return Response({'message': 'Product added successfully'}, status=status.HTTP_200_OK)
        except Appointment.DoesNotExist:
            return Response({'message': 'Appointment does not exist'}, status=status.HTTP_404_NOT_FOUND)


class MakeExpiredAppointment(APIView):
    def post(self, request):
        appointment_id = request.data.get('appointment_id')
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.status = "expired"
            appointment.is_expired = True
            appointment.save()
            return Response({'message': 'Product added successfully'}, status=status.HTTP_200_OK)
        except Appointment.DoesNotExist:
            return Response({'message': 'Appointment does not exist'}, status=status.HTTP_404_NOT_FOUND)
        



class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer