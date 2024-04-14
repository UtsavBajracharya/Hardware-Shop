"""mvc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
    path('',include('login_page.urls')),
    path('',include('Inventory.urls')),
    path('',include('LandingPage.urls')),
    path('',include('OnlineOrders.urls')),
    path('',include('ProductOrders.urls')),
    path('',include('LowInventory.urls')),
    path('',include('Prediction.urls')),
    path('',include('Contact.urls')),
    # path('',include('Billing.urls')),

    # path('admin/', admin.site.urls),
    # path('Billing', views.Billing, name='Billing'),
    # path('Dashboard', views.Dashboard, name='Dashboard'),
    # path('LandingPage', views.LandingPage, name='LandingPage'),
    # path('LowInventory', views.LowInventory, name='LowInventory'),
    # path('OnlineOrders', views.OnlineOrders, name='OnlineOrders'),
    # path('Prediction', views.Prediction, name='Prediction'),
    # path('ProductOrders', views.ProductOrders, name='ProductOrders'),
    # path('Sales', views.Sales, name='Sales'),
    # path('Inventory', views.Inventory, name='Inventory'),
]

