
from django.urls import path
from .views import choose_date_view,choose_time_view,cancel_reservation,choose_service,make_off,make_on

app_name =  "reserve"
urlpatterns = [

    path('selectdate/<str:service>/', choose_date_view, name="select_date"),
    path('selecttime/<str:service>/<str:date>', choose_time_view, name="select_time"),
    path('cancel_reservation/<int:id>', cancel_reservation, name="cancel_time"),
    path('makeoff/', make_off, name="make_off"),
    path('makeon/', make_on, name="make_on"),
    path('', choose_service, name="reserve"),
]
