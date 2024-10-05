from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
from reservation.models import Appointment
from reservation.utils import convert_to_persian_weekday
from datetime import datetime, date
from django.http import JsonResponse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .forms import UpdateUserForm


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'پروفایل شما آپدیت شد')
            return redirect(to="account:login")
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'account/profile.html', {'user_form': user_form})


class Dashboard(View):
    template_name = "account/dashboard.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("account:login")
        
        current_date = date.today()

        all_reservations = Appointment.objects.filter(user=request.user).order_by('-date','status',).all()

        for appointment in all_reservations:
            appointment.reserve_id = appointment.id

        active_reservations = []
        for appointment in all_reservations:
            if appointment.status == "active":
                if appointment.date < current_date:
                    appointment.status="expired"
                    appointment.save()
                else:
                    active_reservations.append(appointment)


        context = {
            "len_active_reservations": len(active_reservations),
            "len_all_reservations": len(all_reservations) ,
            "all_reservations": all_reservations,
        }
        return render(request, self.template_name, context)




def register_view(request):
    template_name = "account/register.html"

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect("account:dashboard")
        else:
            password1=request.POST["password1"]
            password2=request.POST["password2"]
            if password1 != password2:
                messages.error(request, "پسورد و تکرار پسورد یکی نیستند!")
                return redirect("account:register")
            elif len(password1) < 8 :
                messages.error(request, "پسورد باید حداقل 8 کاراکتر باشد")
                return redirect("account:register")
            messages.error(request, "لطفا با اطلاعات درستی فرم ثبت نام را پر کنید!")
            return redirect("account:register")
    form = RegisterForm()
    return render(request, template_name, {"form": form})



def logout_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            logout(request=request)
            messages.info(request, "با موفقیت از اکانت خود خارج شدید")
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
        if not User.objects.filter(username=request.POST["username"]).exists():
            messages.warning(request, 'هیچ یوزری با این نام کاربری ثبت نام شده!')
            return redirect('account:login') 
        if user is not None:
            login(request=request, user=user)
            return redirect("account:dashboard")

        context = {"error_message": "یوزرنیم یا پسورد اشتباه است"}
        messages.warning(request, 'یوزرنیم و پسورد  مطابقت ندارند!')
        return render(request, template_name, context=context)



def check_username(request):
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)