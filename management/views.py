from django.shortcuts import render,redirect
from datetime import date
from reservation.models import Appointment
from django.contrib import messages

# Create your views here.

def list_of_reservations(request):
        if not (request.user.is_superuser or request.user.is_staff):
            messages.error(request, 'شما دسترسی ندارید')
            return redirect("account:login")
        
        template_name = "management/management.html"

        current_date = date.today()
        
        all_reservations = Appointment.objects.filter(status="active").order_by('date', 'timeslot__start_time')
        active_reservations= []
        for appointment in all_reservations:
            if appointment.status == "active":
                if appointment.date < current_date:
                    appointment.status="expired"
                    appointment.save()
                else:
                    active_reservations.append(appointment)
        context = {
              "active_reservations" : active_reservations,
         }
        return render(request,template_name,context)

