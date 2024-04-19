from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
from reservation.models import Appointment




class Dashboard(View):
    template_name = "account/dashboard.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("account:login")

        queryset = Appointment.objects.filter(user=request.user).all()
        for appointment in queryset:
            appointment.start_time = str( appointment.timeslot.start_time)[:-3]
            days_list = ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه", "یک‌شنبه"]
            today_weekday = days_list[appointment.date.weekday()]
            appointment.day = str(today_weekday)
            appointment.reserve_id = appointment.id

            
            

        active_reservations = []
        old_reservations = []
        for appointment in queryset:
            if appointment.is_active == True:
                active_reservations.append(appointment)
            elif appointment.is_active == False:
                old_reservations.append(appointment)

        context = {
            "len_active_reservations": len(active_reservations),
            "len_all_reservations": len(active_reservations) + len(old_reservations),
            "active_reservations": active_reservations,
            "old_reservations": old_reservations,
        }
        return render(request, self.template_name, context)


def register_view(request):
    template_name = "account/register.html"

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("account:dashboard")
        else:
            messages.error(request, "لطفا با اطلاعات درستی فرم ثبت نام را پر کنید!")
            return redirect("account:register")
    form = RegisterForm()
    return render(request, template_name, {"form": form})



def logout_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            logout(request=request)
            return redirect("account:login")


def login_view(request):
    template_name = "account/login.html"
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("account:dashboard")
        return render(request, template_name)
    elif request.method == "POST":
        user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is not None:
            login(request=request, user=user)
            return redirect("account:dashboard")

        context = {"error_message": "یوزرنیم یا پسورد اشتباه است"}
        return render(request, template_name, context=context)
