from django.urls import path
from . import views

urlpatterns = [
    path('AdminLogin/OnlineOrders', views.OnlineOrders, name='onlineOrders'),
    path('orderShipped', views.orderShipped, name='orderShipped'),
    path('cancelOrders', views.cancelOrders, name='cancelOrders'),
    # path('delete_selected_rows', views.deleteProducts, name='deleteProducts'),


]