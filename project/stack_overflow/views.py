from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from stack_overflow.models import Questions,User,Answers

def index(request):
    return render(request,'stack_overflow/home1.html')

def createdata(request):
    all_users = User.objects.all()
    if request.method == 'POST':
        ename = request.POST['uname']
        