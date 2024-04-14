from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
# Create your views here.

class Product:
    def __init__(self, json_data):
        self.product_id = int(json_data['product_id'].strip())
        self.product_name = json_data['product_name'].strip()
        self.category = json_data['category'].strip()
        self.quantity = int(json_data['quantity'].strip())
        self.size = json_data['size'].strip()
        self.description = json_data['description'].strip()
        self.color = json_data['color'].strip()        
        # Remove the dollar sign ('$') and convert the price to float
        self.price = float(json_data['price'].replace('$', '').strip())
        self.product_status = json_data['product_status'].strip()



def Inventory(request):
    inventory_data1 = list(inventory_data.find())
    return render(request, 'Inventory.html',{'inventory_data':inventory_data1})

def addProduct(request):
    record={
        "product_id":request.POST['productNumber'],
        "product_name":request.POST['productName'],
        "description":request.POST['description'],
        "category":request.POST['productCategory'],
        "size":request.POST['size'],
        "color":request.POST['color'],
        "product_status":request.POST['status'],
        "quantity":request.POST['productQuantity'],
        "price":request.POST['productPrice'],
        "product_image":request.POST['productImage']
    }
    record=Product(record)
    record = json.loads(json.dumps(record.__dict__)) #converting the object to a string first then to a dict
    if len(list(inventory_data.find({'product_id':record['product_id']})))== 0:
        
        inventory_data.insert_one(record)
        # JavaScript code to display a popup and redirect to the previous page
        script = """
        <script>
            alert('Product added successfully!');
            window.location.href = "Inventory";
        </script>
        """
        return HttpResponse(script)
    else:
        script = """
        <script>
            alert('Product not added successfully! Cannot take a duplicate Product Number');
            window.location.href = "Inventory";
        </script>
        """
        return HttpResponse(script)


def updateProducts(request):
    updatedRowsList=handle_ajax_request(request)
    print(updatedRowsList)
    for document in updatedRowsList:
        print("Document : ")
        print(document)
        record = Product(document)
        record = json.loads(json.dumps(record.__dict__)) #converting the object to a string first then to a dict

        inventory_data.update_one({'product_id':int(record['product_id'])},{"$set":record})
        inventory_data.update_one({'product_id':record['product_id']},{"$set":record})    
    
    return HttpResponse("request")
    


def handle_ajax_request(request):
    if request.method == 'POST':
        # Assuming the AJAX request sends JSON data
        json_string = request.body.decode('utf-8')  # Get the JSON string from the request

        # Parse the JSON string into a Python data structure
        data = json.loads(json_string)
        print(len)
        # Iterate through the data
        updatedRowsList = []
        for item in data:
            record={
        "product_id":item['SKU'],
        "product_name":item['Name'],
        "description":item['Description'],
        "category":item['Category'],
        "size":item['Size'],
        "color":item['Color'],
        "product_status":item['Status'],
        "quantity":item['Quantity'],
        "price":item['Price'],
    }
            updatedRowsList.append(record)

        # You can then process the data as needed
        # For example, you might want to return a JSON response
        return updatedRowsList
    

def deleteProducts(request):
    updatedRowsList=handle_ajax_request(request)
    print(updatedRowsList)
    for document in updatedRowsList:
        print("Document : ")
        print(document)
        record = Product(document)
        record = json.loads(json.dumps(record.__dict__)) #converting the object to a string first then to a dict
        
        inventory_data.delete_one({'product_id':int(record['product_id'])})
        inventory_data.delete_one({'product_id':record['product_id']})  
    return HttpResponse("Deleted")