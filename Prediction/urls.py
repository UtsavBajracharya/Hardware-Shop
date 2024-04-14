from django.urls import path
from . import views

urlpatterns = [
    path('AdminLogin/Prediction', views.Prediction, name='Prediction')
]