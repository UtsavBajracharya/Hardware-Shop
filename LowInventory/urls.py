from django.urls import path
from . import views

urlpatterns = [
    path('AdminLogin/LowInventory', views.lowInventory, name='lowInventory'),
    path('AdminLogin/SetThreshold', views.setThreshold, name='setThreshold'),


]