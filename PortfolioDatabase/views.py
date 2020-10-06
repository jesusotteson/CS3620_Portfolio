from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby
from .models import Portfolios


# Create your views here.

def Home(request):
    return HttpResponse('Hey! My name is Jp.\nI like programming, video games, and cats.\nIm vibing.')


def Hobbies(request):
    hobby_list = Hobby.objects.all()
    return HttpResponse(hobby_list)


def Portfolio(request):
    portfolio_list = Portfolios.objects.all()
    return HttpResponse(portfolio_list)


def Contact(request):
    return HttpResponse('Email: jesusotteson@mail.weber.edu')
