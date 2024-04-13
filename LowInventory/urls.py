from django.urls import path
from . import views

urlpatterns = [
    path('LowInventory', views.lowInventory, name='lowInventory'),
    path('SetThreshold', views.setThreshold, name='setThreshold'),


]