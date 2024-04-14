from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def Prediction(request):
    sellers_data = list(online_orders_data.find())
    sell_products = []
    sell_categories = []

    products = list(products_data.find())
    
    for item in sellers_data:
        for order in item['order_items']:
            product = products_data.find_one({"product_id": order['product_id']})
            # print(product)
            if product['category'] not in sell_categories : 
                sell_categories.append(product['category'])

            if product not in sell_products : 
                sell_products.append(product)
    
    for item in sellers_data:
        for order in item['order_items']:
            for item in sell_products:
                if item['product_id'] == order['product_id']:
                    if 'ordered_quantity' in item:
                        item['ordered_quantity'] += order['ordered_quantity']
                    else:
                        item['ordered_quantity'] = order['ordered_quantity']

    less_selling = []

    for product in products:
        if product not in sell_products:
            less_selling.append(product)

    return render(request, 'Prediction.html',{'sell_categories': sell_categories, 'sell_products': sell_products, 'less_selling': less_selling})



def Products(productid):
    return products_data.find_one({'product_id': productid})
