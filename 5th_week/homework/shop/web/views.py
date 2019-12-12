from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("哎哟！前台还没准备好，你去找后台吧！ <a href='myadmin/'> >> 点介里呀</a>")