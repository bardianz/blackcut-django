from datetime import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment, Dayoff, Service, TimeSlot
from .utils import date_dict_with_persian_weekday, is_future_date
from django.contrib import messages
from account.utils import check_is_persian


@login_required
def cancel_reservation(request, id):
    if request.method == "POST":
        appointment = Appointment.objects.get(id=id)
        appointment.status = "canceled"
        appointment.save()
        return redirect("account:dashboard")


@login_required
def choose_service(request):
    user_first_name = request.user.first_name
    user_last_name = request.user.last_name

    if not user_first_name and not user_last_name or not check_is_persian(user_first_name) or not check_is_persian(
            user_last_name):
        messages.error(request, 'لطفا نام و نام خانوادگی خود را در قسمت پروفایل بطور کامل و فارسی تکمیل کنید')
        return redirect("account:dashboard")

    user_active_appointments = Appointment.objects.filter(user=request.user, is_active=True).count()
    if user_active_appointments > 3:
        messages.warning(request, 'نوبت های فعال شما بیش از حد مجاز است. لطفا آن ها را کنترل کنید')
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
def choose_date_view(request, service):
    if request.method == "POST":

        date = request.POST.get("date")

        if not service or not date:
            messages.error(request, 'سرویس یا تاریخ به درستی انتخاب نشده')
            return redirect("reserve:select_date")

        if is_future_date(date):
            return redirect("reserve:select_time", date=date, service=service)
        else:
            messages.error(request, 'لطفاً تاریخی قبل از امروز را انتخاب نکنید')
            return redirect("reserve:select_date")

    template_name = "reservation/select_date.html"

    off_days = Dayoff.objects.all()
    all_next_days = date_dict_with_persian_weekday(days_number=14)

    for i in off_days:
        print(i)
        for j in all_next_days:
            if str(i) == str(j['formatted_date']):
                j['status'] = "day-off"

    context = {
        "dates_list": all_next_days,
        "selected_service_name": Service.objects.get(id=service),

        # "active_services": Service.objects.filter(is_active=True)
    }
    # print (context["dates_list"])
    return render(request, template_name, context)


@login_required
def choose_time_view(request, date, service):
    if request.method == "GET":

        all_timeslots = TimeSlot.objects.filter(is_active=True).order_by("start_time").all()
        current_date = str(datetime.today().date())
        current_time = datetime.now().strftime("%H:%M")



        timeslots = []

        for i in all_timeslots:
            start_time_formatted = i.start_time.strftime("%H:%M")
            is_reserved = Appointment.objects.filter(
                date=date,
                timeslot=i,
                status__in=["active", "done", "paid"],
                service=service
            ).exists()

            timeslots.append(
                {
                    "timeslot": i,
                    "start_time_formatted": start_time_formatted,
                    "status": "Reserved" if is_reserved else "Available",
                }
            )
        if current_date == date:
            timeslots = [i for i in timeslots if i['start_time_formatted'] >= current_time]

        context = {
            "total_time_slots": timeslots,
            "selected_date": date,
            "formatted_date": datetime.strptime(date, '%Y-%m-%d').date(),
            "service": service,
            "selected_service_name": Service.objects.get(id=service),
        }
        template_name = "reservation/select_time.html"
        return render(request, template_name, context)

    if request.method == "POST":
        time = request.POST.get("time")
        if time:
            selected_time = TimeSlot.objects.get(start_time=time)

            existing_appointment = Appointment.objects.filter(
                date=date,
                timeslot=selected_time,
                service=Service.objects.get(id=service),
                status__in = ["active", "done", "paid"]
            ).exists()

            if existing_appointment:
                messages.error(request, 'این نوبت قبلاً توسط کاربر دیگری رزرو شده است.')
                return redirect("account:dashboard")

            appoinment = Appointment(
                date=date,
                timeslot=selected_time,
                service=Service.objects.get(id=service),
                user=request.user,
            )
            appoinment.save()
            messages.info(request, 'نوبت شما با موفقیت رزرو شد')
            return redirect("account:dashboard")

    return redirect("reserve:select_date")


@login_required
def make_off(request):
    if not request.user.is_staff:
        return JsonResponse({'error': 'Not Staff User!'}, status=403)

    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request'}, status=400)

    date = request.POST.get('date')

    if not date:
        return JsonResponse({'error': 'No date provided'}, status=400)

    if Appointment.objects.filter(date=date, status="active").exists():
        messages.error(request,
                       'خطا: در روزی که انتخاب شده، نوبت هایی فعال هستند. تا زمانی که فعال باشند امکان تعطیل کردن روز وجود ندارد')
        return HttpResponseRedirect('/')
        # return JsonRلهesponse({'error': 'Appointments exist for this date. Cannot mark as off!'}, status=400)

    if Dayoff.objects.filter(date=date).exists():
        return JsonResponse({'error': 'This date is already marked as off!'}, status=400)

    Dayoff.objects.create(date=date)
    return JsonResponse({'message': 'Date marked as off successfully!'}, status=200)


@login_required
def make_on(request):
    if not request.user.is_staff:
        return JsonResponse({'error': 'Not Staff User!'}, status=403)

    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request'}, status=400)

    date = request.POST.get('date')

    if not date:
        return JsonResponse({'error': 'No date provided'}, status=400)

    deleted_count, _ = Dayoff.objects.filter(date=date).delete()

    if deleted_count > 0:
        return JsonResponse({'message': 'Day successfully opened!'}, status=200)
    else:
        return JsonResponse({'error': 'No records found for the given date!'}, status=404)
