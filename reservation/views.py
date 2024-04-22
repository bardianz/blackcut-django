from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment, Service, TimeSlot
from .utils import date_dict_with_persian_weekday,is_future_date


@login_required
def cancel_reservation(request, id):
    if request.method == "POST":
        appointment = Appointment.objects.get(id=id)
        appointment.is_canceled = True
        appointment.save()
        return redirect("account:dashboard")



@login_required
def choose_date_view(request):

    template_name = "reservation/select_date.html"
    context = {
        "dates_list": date_dict_with_persian_weekday(days_number=14),
        "active_services": Service.objects.filter(is_active=True)
    }

    if request.method == "POST":
        user_active_appointments = Appointment.objects.filter(user=request.user, is_active=True).count()
        if user_active_appointments > 3:
            context["error_message"] = "نوبت های فعال شما بیش از حد مجاز است. لطفا در قسمت پنل کاربری آن ها را کنترل کنید"
            return render(request, template_name, context)

        date = request.POST.get("date")
        service = request.POST.get("service")
        

        print(date, type(date))
        print("----------")

        # Check service and date existence
        if not service or not date:
            context["error_message"] = "سرویس یا تاریخ انتخاب نشده"
            return render(request, template_name, context)

        # # Convert datetime to str
        # try:
        #     date = datetime.strptime(date, "%Y-%m-%d")

            
        # except Exception as e:
        #     context["error_message"] = f"مشکلی در تبدیل تاریخ پیش آمده: {e}"
        #     return render(request, template_name, context)

        if is_future_date(date):
            return redirect("reserve:select_time", date=date, service=service)
        else:
            context["error_message"] = "لطفاً تاریخی قبل از امروز را انتخاب نکنید"

    return render(request, template_name, context)




@login_required
def choose_time_view(request, date, service):
    if request.method == "GET":


        all_timeslots = TimeSlot.objects.order_by("start_time").all()

        timeslots = []

        for i in all_timeslots:
            start_time_formatted = i.start_time.strftime("%H:%M")
            is_reserved = Appointment.objects.filter(date=date,timeslot=i,is_active=True,is_canceled=False,
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
