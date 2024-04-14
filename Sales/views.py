from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def Sales(request):
    online_orders_data = list(online_orders.find({'status': 'Processed'}))
    order_product = []

    for order in online_orders_data:
        order_product.extend(order['order_items'])

    total_ordered_quantity = {}

    # Iterate through each order item
    for item in order_product:
        product_id = item['product_id']
        ordered_quantity = item['ordered_quantity']
        
        # Update total ordered quantity for the product_id
        if product_id in total_ordered_quantity:
            total_ordered_quantity[product_id] += ordered_quantity
        else:
            total_ordered_quantity[product_id] = ordered_quantity

    # Create a new list of dictionaries with summed quantities
    unique_items = [{'product_id': product_id, 'ordered_quantity': quantity} for product_id, quantity in total_ordered_quantity.items()]

    for item in unique_items:
        product_details = get_product_details(item['product_id'])
        if product_details:
            item['product_name'] = product_details.get('product_name', 'Unknown')
            item['category'] = product_details.get('category', 'Unknown')
            item['size'] = product_details.get('size', 'Unknown')
            item['product_status'] = product_details.get('product_status', 'Unknown')
            item['price'] = product_details.get('price', 0)
            item['discount'] = product_details.get('discount', 0)
            item['grossTotal'] = round(float(item['price']) * float(item['ordered_quantity']), 2)
            item['netTotal'] = round(float(item['grossTotal']) - float(item['discount']), 2)
    print(unique_items)
    return render(request, 'Sales.html', {'sold_product': unique_items})

def get_product_details(product_id):
    product_collection = db['products']  # Replace 'products' with your actual collection name
    product = product_collection.find_one({'product_id': product_id})
    return product
