import random
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import random

# Create your views here.
def productOrders(request):
    product_orders_data = product_orders.find()
    return render(request, 'ProductOrders.html',{'product_orders':product_orders_data})

class ProductOrder:
    def __init__(self, order_id, product_id, product_name, description,ordered_date, vendor, status, estimated_arrival,ordered_quantity,price ):
        self.order_id = int(order_id)
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.ordered_date = ordered_date
        self.vendor = vendor
        self.status = status
        self.estimated_arrival = estimated_arrival
        self.ordered_quantity = ordered_quantity
        self.price = price



def fetch_product(request, product_id):
    try:
        product = inventory_data.find({'product_id':product_id})
        data = {
            "SKU": product.product_id,
            "Name": product.product_name,
            "Description": product.description,
            "Category": product.category,
            "Size": product.size,
            "Color": product.color,
            "Status": product.product_status,
            "Quantity": product.quantity,
            "Price": product.price
        }
        return JsonResponse(data)
    except product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)





def recieveOrders(request):
    print(str(request))
    updatedRowsList=handle_ajax_request(request)
    print(updatedRowsList)
    for document in updatedRowsList:
        record = ProductOrder(document['order_id'],document['product_id'],document['product_name'],document['description'],document['ordered_date'],document['vendor'],document['status'],document['estimated_arrival'],document['ordered_quantity'],document['price'])
        record = json.loads(json.dumps(record.__dict__)) #converting the object to a string first then to a dict
        product_orders.update_one({'order_id':int(record['order_id'])},{"$set":{'status': 'Recieved'}})
       
    return HttpResponse("request")
def cancelOrders(request):
    print(str(request))
    updatedRowsList=handle_ajax_request(request)
    print(updatedRowsList)
    for document in updatedRowsList:
        record = ProductOrder(document['order_id'],document['product_id'],document['product_name'],document['description'],document['ordered_date'],document['vendor'],document['status'],document['estimated_arrival'],document['ordered_quantity'],document['price'])
        record = json.loads(json.dumps(record.__dict__)) #converting the object to a string first then to a dict
        product_orders.update_one({'order_id':int(record['order_id'])},{"$set":{'status': 'Cancelled'}})
       
    return HttpResponse("request")

def addProductOrders(request):
    return HttpResponse(request)

def handle_ajax_request(request):
    if request.method == 'POST':
        # Assuming the AJAX request sends JSON data
        json_string = request.body.decode('utf-8')  # Get the JSON string from the request
        # Parse the JSON string into a Python data structure
        data = json.loads(json_string)
        
        # Iterate through the data
        updatedRowsList = []
        for item in data:
            record = {
                "order_id": item['Order ID'],
                "product_id": item['SKU'],
                "product_name": item['Name'],
                "description": item['Description'],
                "ordered_date": item['Ordered Date'],
                "vendor": item['Vendor'],
                "status": item['Status'],
                "estimated_arrival": item['Estimated Arrival'],
                "ordered_quantity": item['Ordered Quantity'],
                'price':item['Price']
                
            }

            updatedRowsList.append(record)

        return updatedRowsList
    