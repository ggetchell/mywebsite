from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"
    
class AboutPageView(TemplateView):
    template_name = "about.html"
    
class PortfolioPageView(TemplateView):
    template_name = "portfolio.html"
    
class ContactPageView(TemplateView):
    template_name = "contact.html"