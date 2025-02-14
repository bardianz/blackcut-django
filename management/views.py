from django.shortcuts import render,redirect
from datetime import date
from reservation.models import Appointment
from django.contrib import messages

# Create your views here.

def list_of_active_reservations(request):
        if not (request.user.is_superuser or request.user.is_staff):
            messages.error(request, 'شما دسترسی ندارید')
            return redirect("account:login")
        
        template_name = "management/management.html"

        current_date = date.today()
        
        reservations = Appointment.objects.filter(status="active").order_by('date', 'timeslot__start_time')
        active_reservations= []
        for appointment in reservations:
            if appointment.status == "active":
                if appointment.date < current_date:
                    appointment.status="expired"
                    appointment.save()
                else:
                    active_reservations.append(appointment)
        context = {
              "active_reservations" : active_reservations,
              "page":"active",
         }
        return render(request,template_name,context)


def list_of_all_reservations(request):
        if not (request.user.is_superuser or request.user.is_staff):
            messages.error(request, 'شما دسترسی ندارید')
            return redirect("account:login")
        
        template_name = "management/management.html"

        current_date = date.today()
        all_reservations = Appointment.objects.exclude(status__in=["canceled"]).order_by('-date', 'timeslot__start_time')[:20]
        active_reservations= []
        for appointment in all_reservations:
            if appointment.status == "active":
                if appointment.date < current_date:
                    appointment.status="expired"
                    appointment.save()
            active_reservations.append(appointment)

        context = {
              "active_reservations" : active_reservations,
              "page":"all",
         }
        return render(request,template_name,context)


def list_of_done_reservations(request):
        if not (request.user.is_superuser or request.user.is_staff):
            messages.error(request, 'شما دسترسی ندارید')
            return redirect("account:login")
        
        template_name = "management/management.html"

        current_date = date.today()
        all_reservations = Appointment.objects.filter(status="done").order_by('date', 'timeslot__start_time')
        active_reservations= []
        for appointment in all_reservations:
            if appointment.status == "active":
                if appointment.date < current_date:
                    appointment.status="expired"
                    appointment.save()
            active_reservations.append(appointment)

        context = {
              "active_reservations" : active_reservations,
              "page":"done",
         }
        return render(request,template_name,context)