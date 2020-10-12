from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Hobby
from .models import Portfolio


# Create your views here.

def Home(request):
    return render(request, 'home/index.html')


def Hobbies(request):
    hobby_list = Hobby.objects.all()
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


def Portfolios(request):
    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolio_list': portfolio_list,
    }
    return render(request, 'portfolios/index.html', context)


def portfolio_detail(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'portfolios/detail.html', context)


def Contact(request):
    return render(request, 'contact/index.html')


def contact_item(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:Home')

    return render(request, 'contact/contact-form.html', {'form': form})
