from django.urls import path
from . import views

urlpatterns = [
    path('AdminLogin/Contact', views.Contact, name='Contact'),

]
