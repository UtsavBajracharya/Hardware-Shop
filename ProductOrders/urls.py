from django.urls import path
from . import views

urlpatterns = [
    path('ProductOrders', views.productOrders, name='productOrders'),
    path('cancelProductOrders', views.cancelOrders, name='cancelOrders'),
    path('recieveProductOrders', views.recieveOrders, name='recieveOrders'),
    path('addProductOrder', views.addProductOrders, name='addProductOrders'),
    # path('orderShipped', views.orderShipped, name='orderShipped'),
    # path('cancelOrders', views.cancelOrders, name='cancelOrders'),
    # path('delete_selected_rows', views.deleteProducts, name='deleteProducts'),


]