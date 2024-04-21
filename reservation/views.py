from django.shortcuts import render,redirect
from .forms import DatePickerForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Appointment,Service,TimeSlot
from utils import jalali
from utils.jalali_weekday import jalali_numerical_convertor



@login_required
def cancel_reservation(request,id):
    if request.method == "POST":
        appointment = Appointment.objects.get(id=id)  
        appointment.is_canceled = True
        appointment.save()
        return redirect("account:dashboard")


@login_required
def choose_date_view(request):

    template_name="reservation/select_date.html"
    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%Y-%m-%d")
    today = jalali_numerical_convertor(current_date)
    days_list = ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه", "یک‌شنبه"]
    today_weekday = days_list[current_datetime.weekday()]

    print(today)

    form = DatePickerForm()  

    context = {
        'form':form ,
        'today':today, 
        'today_weekday' : today_weekday,
        }
    if request.method == "POST":
        
        user_active_appointment_count = Appointment.objects.filter(user=request.user ,is_active=True).count()
        if user_active_appointment_count>3:
            context['error_message'] =  "نوبت های فعال شما بیش از حد مجاز است. لطفا در قسمت پنل کاربری آن ها را کنترل کنید"
            return render(request,template_name,context)

        date = request.POST.get('date')
        service = request.POST.get('service')


        if not date:
            context['error_message'] =  "لطفا تاریخ را پر کنید"
            return render(request,template_name,context)
        
        if not service:
            context['error_message'] =  "لطفا بخش سرویس را با دقت پر کنید"
            return render(request,template_name,context)
        

        selected_date = datetime.strptime(date, '%Y-%m-%d').date()
        today_date = datetime.strptime(str(today), '%Y-%m-%d').date()
        print(selected_date)
        print(today_date)
        if selected_date >= today_date:
            print("OK")
            return redirect("reserve:select_time",date = date,service = service)
        
        context['error_message'] =  "لطفا تاریخی قبل از امروز را انتخاب نکنید"

    return render(request,template_name,context)


@login_required
def choose_time_view(request, date,service):
    if request.method == "GET":
        # if date and service:
            
        #     current_datetime = datetime.now()
        #     current_date = current_datetime.strftime("%Y-%m-%d")
        #     today = jalali_numerical_convertor(current_date)
            
        #     selected_date = datetime.strptime(date, '%Y-%m-%d').date()
        #     today_date = datetime.strptime(str(today), '%Y-%m-%d').date()
        #     time_slot_generator = TimeSlotGenerator(["8:30", "16:30"], ["13:30", "21:30"], 30)

        #     if selected_date == today_date:      

        #         current_time = datetime.now().time()
        #         current_rounded_time = round_up_to_nearest_half_hour(current_time)

        #         time_slot_generator.remove_past_time_slots(current_rounded_time)

            gregorian_date = jalali.Persian(str(date) ).gregorian_datetime()
            selected_slots = TimeSlot.objects.filter(is_active=True).all()

            # for i in selected_slots:
            #     # بررسی آیا نوبتی برای تاریخ مورد نظر وجود دارد یا خیر
            #     is_reserved = Appointment.objects.filter(
            #         date=gregorian_date,
            #         timeslot=i.timeslot_id, 
            #     ).exists()

            #     i['status'] = 'Reserved' if is_reserved else 'Available'
            all_timeslots = TimeSlot.objects.all()

            timeslots = []

            for i in all_timeslots:
                start_time_formatted = i.start_time.strftime("%H:%M") 
                is_reserved = Appointment.objects.filter(
                    date=gregorian_date,
                    timeslot=i,
                    is_active=True,
                    is_canceled=False,
                ).exists()

                timeslots.append({
                    'timeslot': i,
                    'start_time_formatted' : start_time_formatted,
                    'status': 'Reserved' if is_reserved else 'Available'
                })

            context = {
                'total_time_slots':timeslots,
                'selected_date': date,
                "service" : service ,
            }
            template_name="reservation/select_time.html"
            return render(request,template_name,context)
    
    if request.method == "POST":
        time = request.POST.get('time')
        if time:
            selected_time = TimeSlot.objects.get(start_time=time)
            gregorian_edate = jalali.Persian(str(date) ).gregorian_datetime()
            appoinment = Appointment(
                date=gregorian_edate,
                timeslot=selected_time,
                service = Service.objects.get(id=service) , 
                user = request.user, )
            appoinment.save()
            return redirect("account:dashboard")

        print("NO DATA")
        # Appointment.objects.create()
    return redirect("reserve:select_date")

