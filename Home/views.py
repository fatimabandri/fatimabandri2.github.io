from django.shortcuts import render
from .models import Home

def home(request):
    data = Home.objects.all()
    return render(request, 'index.html', {'data': data})