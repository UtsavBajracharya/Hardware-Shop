from datetime import datetime
import random
from urllib.parse import parse_qs
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



def fetchProduct(request):
    product_id = str(request.body.decode('utf-8')).strip('"')
    product = list(inventory_data.find({'product_id':int(product_id)}))[0]
    vendor=vendors.find()
    vendor_names=[]
    for item in vendor:
        vendor_names.append(item['vendor_name'])
    vend= list(vendor_names)

    data = {
        "SKU": product['product_id'],
        "Name": product['product_name'],
        "Description": product['description'],
        "Category": product['category'],
        "Size": product['size'],
        "Color": product['color'],
        "Status": product['product_status'],
        "Quantity": product['quantity'],
        "Price": product['price'],
        "vendor":vend
    }
    return JsonResponse(data)






def recieveOrders(request):
    updatedRowsList=handle_ajax_request(request)
    for document in updatedRowsList:
        record = ProductOrder(document['order_id'],document['product_id'],document['product_name'],document['description'],document['ordered_date'],document['vendor'],document['status'],document['estimated_arrival'],document['ordered_quantity'],document['price'])
        record = json.loads(json.dumps(record.__dict__)) #converting the object to a string first then to a dict
        product_orders.update_one({'order_id':int(record['order_id'])},{"$set":{'status': 'Recieved'}})
       
    return HttpResponse("request")

def cancelOrders(request):
    updatedRowsList=handle_ajax_request(request)
    for document in updatedRowsList:
        record = ProductOrder(document['order_id'],document['product_id'],document['product_name'],document['description'],document['ordered_date'],document['vendor'],document['status'],document['estimated_arrival'],document['ordered_quantity'],document['price'])
        record = json.loads(json.dumps(record.__dict__)) #converting the object to a string first then to a dict
        product_orders.update_one({'order_id':int(record['order_id'])},{"$set":{'status': 'Cancelled'}})
       
    return HttpResponse("request")

def generate_new_order_id():
    # Find the latest order
    latest_order = product_orders.find_one({}, sort=[('order_id', -1)])
    if latest_order:
        latest_order_id = latest_order['order_id']
        new_order_id = int(latest_order_id) + 1
    else:
        # If no orders exist yet, start from 1
        new_order_id = 1

    return new_order_id

def addProductOrders(request):
    # json_string = request.body.decode('utf-8')
    # query_dict = parse_qs(json_string)
    # data = json.dumps(query_dict)
    order_id=generate_new_order_id()

    current_date = datetime.now().date().strftime("%d-%m-%Y")
    productOrder= ProductOrder(order_id, request.POST['productNumber'],request.POST['productName'], request.POST['description'],current_date, request.POST['vendor'], 'Pending', "NA",request.POST['orderQuantity'],request.POST['productPrice'] )
    product_orders.insert_one(productOrder.__dict__)
    script = """
        <script>
            alert('Order Placed successfully!!!');
            window.location.href = "ProductOrders";
        </script>
        """
    return HttpResponse(script)

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
    