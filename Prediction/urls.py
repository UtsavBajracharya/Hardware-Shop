from django.urls import path
from . import views

urlpatterns = [
    path('Prediction', views.Prediction, name='Prediction')
]