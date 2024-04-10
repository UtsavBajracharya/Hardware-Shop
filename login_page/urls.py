from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('userAuthentication', views.userAuthentication, name='userAuthentication'),
    path('addUser', views.addUser, name='addUser'),
    path('showRecords', views.showRecords, name='showRecords'),
    path('toLand',views.toLand, name='toLand' ),
    

]