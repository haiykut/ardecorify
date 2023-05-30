# example/views.py
from django.contrib.auth.models import User
from datetime import datetime
import json
from example.models import Furniture1
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os

def index(request):
    time = datetime.now()
    
    
    if request.method == 'POST':

       
            username = request.POST['username']
            password= request.POST['password']
            repassword= request.POST['repassword']
            message=""
            if len(username)==0 or len(password)==0:
                message="Kullanıcı adı veya şifre boş bırakılamaz."
                
            elif password!=repassword:
                message="Şifre eşleşmedi."
                
            else:
                try:
                    module_dir = os.path.dirname(__file__)  # get current directory
                    file_path = os.path.join(module_dir, 'static/furnitures.json')
                    f = open(file_path)
  
                    data = json.load(f)
  
                    user = User.objects.create_user(username = username , password = password)
                    user.save()
                    user2= Furniture1(usern=username,furn=data)
                    user2.save()

                    message="Kayıt Başarılı"
                    
                except Exception as error:
                    #message="Kullanıcı adı zaten kullanımda."
                    message=error

            return render(request,'index.html',{"message":message})

    else:
        message="Kayıt Ol"
        return render(request, 'index.html',{'message':message})
HttpResponse("")


@csrf_exempt
def login(request):
    
        if request.method == 'POST':
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)     
            data=body
            username = data['user']["username"]
            password = data['user']["password"]
            user = auth.authenticate(username = username, password =password  )

            if user is not None:
                auth.login(request , user)
                control=True
                return HttpResponse("true"  )
 
            else:
                control=False
                return HttpResponse("false")            
       
        else:
            return render(request,'login.html')

def logout_request(request):
    auth.logout(request)
    return redirect('index')



@csrf_exempt
def furniturerequest(request):
    try:
        if request.method == 'POST':
            usernn = None
            if request.user.is_authenticated:
                try:
                    body_unicode = request.body.decode('utf-8')
                    body = json.loads(body_unicode)
                    usernn = request.user.username
                    Furniture1.objects.filter(usern=usernn).update(furn=body)
                    return HttpResponse("success")
                except Exception as error:
                    return HttpResponse(error)
            else:
                return  HttpResponse("giris yapmadin")
        else:
            return HttpResponse("post metodu degil")
    except Exception as error:
        HttpResponse(error)