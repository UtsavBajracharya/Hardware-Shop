from django.urls import path
from . import views

urlpatterns = [
    path('AdminLogin/Inventory', views.Inventory, name='Inventory'),
    path('AdminLogin/addProduct', views.addProduct, name='addProduct'),
    path('AdminLogin/update_selected_rows', views.updateProducts, name='updateProducts'),
    path('AdminLogin/delete_selected_rows', views.deleteProducts, name='deleteProducts'),


]