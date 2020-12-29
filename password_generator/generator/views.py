from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):



    characters = list('abcdefghijklmnopqrstuvwxyz')

    length=int(request.GET.get('length',8))

    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWYZX'))
    if request.GET.get('Numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('Special Characters'):
        characters.extend(list('!@#$%^&*'))
    thepassword = ''
    for x in range(length):
        thepassword+=random.choice(characters)

    return render(request,'generator/password.html',{'password':thepassword})

def About(request):
    return render(request,'generator/About.html')