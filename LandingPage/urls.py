from django.urls import path
from . import views

urlpatterns = [
    path('AdminLogin/LandingPage', views.LandingPage, name='LandingPage'),
    path('AdminLogin/', views.Login, name='Login'),
    path('AdminLogin/login', views.RedirectLogin, name='RedirectLogin')
]