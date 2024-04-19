from django.urls import path
from .views import ActiveAppointments,AllProducts

urlpatterns = [
    path('allproducts/', AllProducts.as_view(), name='allproducts'),
    path('activeappointments/', ActiveAppointments.as_view(), name='activeappointments'),
]
