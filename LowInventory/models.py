from django.db import models
from db_connection import db

# Create your models here.
inventory_data= db['products']
threshold_data= db['threshold']
product_orders_data = db['product_orders']