from django.urls import path
from . import views

urlpatterns = [
    path('AdminLogin/ProductOrders', views.productOrders, name='productOrders'),
    path('cancelProductOrders', views.cancelOrders, name='cancelOrders'),
    path('recieveProductOrders', views.recieveOrders, name='recieveOrders'),
    path('addProductOrder', views.addProductOrders, name='addProductOrders'),
    path('fetchProduct', views.fetchProduct, name='fetchProduct'),
    # path('orderShipped', views.orderShipped, name='orderShipped'),
    # path('cancelOrders', views.cancelOrders, name='cancelOrders'),
    # path('delete_selected_rows', views.deleteProducts, name='deleteProducts'),


]