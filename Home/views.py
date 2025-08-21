from django.shortcuts import render
from.models import Home
# Create your views here.
def home(request):
    data=Home.objects.all()
    return render(request,'index.html',{'data':data})
    