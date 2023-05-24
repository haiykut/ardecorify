# example/views.py
from django.contrib.auth.models import User
from datetime import datetime
import json
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
def index(request):
    now = datetime.now()
    f = open('user.json')

    data = json.load(f)
    username = data['user']["username"]
    password = data['user']["password"]
    user = authenticate(request,username = username,password = password)
    if user is not None:
        control=True
    else:
        control=False
        
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>,
            <p>return: { control }.</p>
        </body>
    </html>
    '''   
        
    return HttpResponse(html)
HttpResponse("")