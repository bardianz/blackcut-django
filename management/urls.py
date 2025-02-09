
from django.urls import path
from .views import list_of_reservations

app_name =  "reserve"
urlpatterns = [

    path('', list_of_reservations, name="list_of_reservations"),
]
