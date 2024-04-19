from django.urls import path
from .views import Dashboard,login_view,logout_view,register_view

app_name= 'account'


urlpatterns = [

    path('', Dashboard.as_view(),name="dashboard"),
    path('register/', register_view,name="register"),
    path('login/', login_view,name="login"),
    path('logout/', logout_view,name="logout"),

]

SOCIAL_AUTH_URL_NAMESPACE = 'social'
