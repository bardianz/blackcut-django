from django.urls import path
from .views import ActiveAppointments,AllProducts,AddProductToAppointment,AllAppointments, CategoryListView,remove_product_from_appointment,MakeDoneAppointment,MakePaidAppointment

urlpatterns = [
    path('allproducts/', AllProducts.as_view(), name='allproducts'),
    path('activeappointments/', ActiveAppointments.as_view(), name='activeappointments'),
    path('allappointments/', AllAppointments.as_view(), name='allappointments'),
    path('add_product_to_appointment/', AddProductToAppointment.as_view(), name='add_product_to_appointment'),
    path('remove_product_from_appointment/', remove_product_from_appointment, name='remove_product_from_appointment'),
    path('make_done_appointment/', MakeDoneAppointment.as_view(), name='make_done_appointment'),
    path('make_paid_appointment/', MakePaidAppointment.as_view(), name='make_paid_appointment'),
    path('categories/', CategoryListView.as_view(), name='category_list'),

]
