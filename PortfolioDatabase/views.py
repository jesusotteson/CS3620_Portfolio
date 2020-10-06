from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby
from .models import Portfolios
from django.template import loader


# Create your views here.

def Home(request):
    template = loader.get_template('home/index.html')
    return render(request, 'home/index.html')


def Hobbies(request):
    hobby_list = Hobby.objects.all()
    template = loader.get_template('hobbies/index.html')
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, 'hobbies/index.html', context)


def hobby_detail(request, hobby_id):
    hobby = Hobby.objects.get(pk=hobby_id)
    context = {
        'hobby': hobby
    }
    return render(request, 'hobbies/detail.html', context)


def Portfolio(request):
    portfolio_list = Portfolios.objects.all()
    template = loader.get_template('portfolios/index.html')
    context = {
        'portfolio_list': portfolio_list,
    }
    return render(request, 'portfolios/index.html', context)


def portfolio_detail(request, portfolio_id):
    portfolio = Portfolios.objects.get(pk=portfolio_id)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'portfolios/detail.html', context)


def Contact(request):
    template = loader.get_template('contact/index.html')
    return render(request, 'contact/index.html')
