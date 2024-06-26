from django.urls import path
from .views import ActiveAppointments,AllProducts,AddProductToAppointment,remove_product_from_appointment

urlpatterns = [
    path('allproducts/', AllProducts.as_view(), name='allproducts'),
    path('activeappointments/', ActiveAppointments.as_view(), name='activeappointments'),
    path('add_product_to_appointment/', AddProductToAppointment.as_view(), name='add_product_to_appointment'),
    path('remove_product_from_appointment/', remove_product_from_appointment, name='remove_product_from_appointment'),
]
