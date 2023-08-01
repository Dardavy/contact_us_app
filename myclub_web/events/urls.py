from django.urls import path
from .import views

urlpatterns = [
    path('', views.contact, name="contact"),
    # path('', views.home, name="home"),
    # path('contact.html', views.contact, name="contact"),
    # path('myuser_pdf', views.myuser_pdf, name="myuser_pdf"),
]