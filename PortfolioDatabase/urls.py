from . import views
from django.urls import path

app_name = 'PortfolioDatabase'
urlpatterns = [
    path('', views.Home, name='Home'),
    path('hobbies/', views.Hobbies, name='Hobbies'),
    path('<int:hobby_id>', views.hobby_detail, name="hobby_detail"),
    path('portfolio/', views.Portfolios, name='Portfolios'),
    path('add_portfolio/', views.portfolio_item, name="portfolio_item"),
    path('update/<int:id>', views.update_portfolio, name="update_portfolio"),
    path('delete/<int:id>', views.delete_portfolio, name="delete_portfolio"),
    path('<int:portfolio_id>/portfolio_detail', views.portfolio_detail, name="portfolio_detail"),
    path('contact/', views.Contact, name='Contact'),
    path('add_contact/', views.contact_item, name="contact_item")
]
