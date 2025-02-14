
from django.urls import path
from .views import list_of_active_reservations,list_of_all_reservations,list_of_done_reservations

app_name =  "management"
urlpatterns = [

    path('', list_of_active_reservations, name="list_of_reservations"),
    path('all/', list_of_all_reservations, name="list_of_all_reservations"),
    path('done/', list_of_done_reservations, name="list_of_done_reservations"),
]
