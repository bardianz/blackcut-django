from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment, Service, TimeSlot
from .utils import date_dict_with_persian_weekday,is_future_date
from django.contrib import messages


@login_required
def cancel_reservation(request, id):
    if request.method == "POST":
        appointment = Appointment.objects.get(id=id)
        appointment.is_canceled = True
        appointment.status = "canceled"
        appointment.save()
        return redirect("account:dashboard")


def choose_service(request):


    
    if not request.user.first_name and not request.user.last_name :
        messages.error(request, 'لطفا نام و نام خانوادگی خود را در قسمت پروفایل به درستی تکمیل کنید')
        return redirect("account:dashboard")
    
    user_active_appointments = Appointment.objects.filter(user=request.user, is_active=True).count()
    if user_active_appointments > 3:
        messages.error(request, 'نوبت های فعال شما بیش از حد مجاز است. لطفا آن ها را کنترل کنید')
        return redirect("account:dashboard")

    
    template_name = "reservation/select_service.html"
    context = {
        "all_services": Service.objects.filter
    }

    if request.method == "POST":
        service = request.POST.get("service")
        if service:
            return redirect("reserve:select_date", service=service)



    return render(request, template_name, context)



@login_required
def choose_date_view(request,service):

    template_name = "reservation/select_date.html"
    context = {
        "dates_list": date_dict_with_persian_weekday(days_number=14),
        "selected_service_name": Service.objects.get(id=service),

        # "active_services": Service.objects.filter(is_active=True)
    }

    if request.method == "POST":
  
        date = request.POST.get("date")
        
        if not service or not date:
            context["error_message"] = "سرویس یا تاریخ انتخاب نشده"
            return render(request, template_name, context)

        if is_future_date(date):
            return redirect("reserve:select_time", date=date, service=service)
        else:
            context["error_message"] = "لطفاً تاریخی قبل از امروز را انتخاب نکنید"

    # if not request.user.first_name and not request.user.last_name :
    #     messages.error(request, 'لطفا نام و نام خانوادگی خود را در قسمت پروفایل به درستی تکمیل کنید')
    #     return redirect("account:dashboard")
        
    return render(request, template_name, context)




@login_required
def choose_time_view(request, date, service):
    if request.method == "GET":


        all_timeslots = TimeSlot.objects.order_by("start_time").all()

        timeslots = []

        for i in all_timeslots:
            start_time_formatted = i.start_time.strftime("%H:%M")
            is_reserved = Appointment.objects.filter(date=date,timeslot=i,is_active=True,is_canceled=False,service=service
            ).exists()

            timeslots.append(
                {
                    "timeslot": i,
                    "start_time_formatted": start_time_formatted,
                    "status": "Reserved" if is_reserved else "Available",
                }
            )

        context = {
            "total_time_slots": timeslots,
            "selected_date": date,
            "service": service,
        }
        template_name = "reservation/select_time.html"
        return render(request, template_name, context)

    if request.method == "POST":
        time = request.POST.get("time")
        if time:
            selected_time = TimeSlot.objects.get(start_time=time)

            appoinment = Appointment(
                date=date,
                timeslot=selected_time,
                service=Service.objects.get(id=service),
                user=request.user,
            )
            appoinment.save()
            return redirect("account:dashboard")

        print("NO DATA")
        # Appointment.objects.create()
    return redirect("reserve:select_date")
