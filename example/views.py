# example/views.py
from django.contrib.auth.models import User
from datetime import datetime
import json
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
def index(request):
    time = datetime.now()
    
    return render(request, 'index.html',{'time':time})
HttpResponse("")
def register(request):

    if request.method == 'POST':

       
            username = request.POST['username']
            password= request.POST['password']
            
            try:
                user = User.objects.create_user(username = username , password = password)
            except:
                return render(request,'register.html')
            user.save()
            
            return redirect('login')

    else:
        return render(request,'register.html')

def login(request):
    
#   if request.method =="POST":
#        username = request.POST["username"]  
#        password = request.POST["password"]
        if request.method == 'POST':
            username = request.POST["username"]  
            password = request.POST["password"]        
#           data=request.body.json.loads()
#           username = data['user']["username"]
#           password = data['user']["password"]
            user = auth.authenticate(username = username, password =password  )

            if user is not None:
                auth.login(request , user)
                control=True
                return redirect('index',{"control":control})    
            else:
                control=False
                return redirect('login',{"control":control})
                
        else:
            return render(request,'login.html')

def logout_request(request):
    auth.logout(request)
    return redirect('index')