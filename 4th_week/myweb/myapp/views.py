from django.shortcuts import render
from django.http  import HttpResponse
from myapp.models import Stu

# Create your views here.

def index(request):
    return HttpResponse("Hello, Django")


# 使用 stu 表数据

def stu(request):
    mod = Stu.objects
    list = mod.all()
    print(list)

    return HttpResponse("okay")

