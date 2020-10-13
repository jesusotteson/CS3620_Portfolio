from django import forms
from .models import Contact
from .models import Portfolio


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_email', 'contact_message']


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['portfolio_name', 'portfolio_description', 'portfolio_image']
