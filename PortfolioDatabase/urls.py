from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name='Home'),
    path('', views.Hobbies, name='Hobbies'),
    path('', views.Portfolio, name='Portfolio'),
    path('', views.Contact, name='Contact')
]