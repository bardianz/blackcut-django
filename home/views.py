from django.shortcuts import render
from .models import HomePage



def home_page_view(request):
    homepage_data = HomePage.objects.all()
    context = {'homepage_data': homepage_data}
    return render(request, 'home/index.html', context)
