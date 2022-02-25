from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'vulko.html')
def home(request):
    return render(request,'morgana.html')
def signup(request):
    return render(request,'sign.html')
 
 
# Create your views here.
