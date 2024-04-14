from django.urls import path
from . import views

urlpatterns = [
    path('AdminLogin/Sales', views.Sales, name='Sales')
]