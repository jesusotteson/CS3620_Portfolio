from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return HttpResponse('Hey! My name is Jp.\nI like programming, video games, and cats.\nIm vibing.')

def Hobbies(request):
    return

def Portfolio(request):
    return

def Contact(request):
    return