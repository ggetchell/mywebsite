# staticsite/example/urls.py

from django.conf.urls import url
from example import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^portfolio/$', views.PortfolioPageView.as_view(), name='portfolio'),
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
]