from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import users



def index(request):
    return render(request,'vulko.html')
def home(request):
    id=request.session['userid']
    userdata=users.objects.get(id=id)
    return render(request,'morgana.html',{"userdetails":userdata})

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

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            data=users.objects.get(username=username, paswword=password)
            request.session['userid']=data.id
            return redirect('/home')
        except users.DoesNotExist:
            return render(request,'oblivion.html',{'status':'login failed'})    
    else:
              return render(request,'oblivion.html') 


def viewUSers(request):
    userdata=users.objects.all()
    return render(request,'viewUsers.html',{"userdata": userdata}) 

def updateUser(request, id):
    if request.method =="POST":
        fullname=request.POST['fullname']
        address=request.POST['address']
        age=request.POST['age']
        username=request.POST['username']
        password=request.POST['password']
        userdetils=users.objects.filter(id=id).update(fullname=fullname, address=address, paswword=password,age=age,username=username)
        return redirect('/viewUsers/')
    else:
        userdata=users.objects.get(id=id)
        return render(request,'updateuser.html', {"userdetails": userdata}) 

def deleteUser(request, id):
    users.objects.filter(id=id).delete()
    return redirect('/viewUsers/')

      
    

 

         
 
 
# Create your views here.
