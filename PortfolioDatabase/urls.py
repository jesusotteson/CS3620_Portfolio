from . import views
from django.urls import path

app_name = 'PortfolioDatabase'
urlpatterns = [
    path('', views.Home, name='Home'),
    path('hobbies/', views.Hobbies, name='Hobbies'),
    path('<int:hobby_id>', views.hobby_detail, name="hobby_detail"),
    path('portfolio/', views.Portfolio, name='Portfolio'),
    path('<int:portfolio_id>/portfolio_detail', views.portfolio_detail, name="portfolio_detail"),
    path('contact/', views.Contact, name='Contact')
]
