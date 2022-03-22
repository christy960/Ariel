from django.shortcuts import render
from django.http import HttpResponse
from .models import users
from .models import Users


def index(request):
    return render(request,'vulko.html')
def home(request):
    return render(request,'morgana.html')
def signup(request):
    return render(request,'sign.html')
def signup6(request):
        return render(request,'everdeen.html')  

def signup4(request):
     if request.method == 'POST':
         name=request.POST['fullname']
         username=request.POST['username']
         password=request.POST['password']
         address=request.POST['address']
         age=request.POST['age']
         userdata=users(username=username,paswword=password,fullname=name,address=address, age=age)
         userdata.save()
        
         return render(request,'test.html')  
     else:
         return render(request,'test.html')      
 
 
# Create your views here.
