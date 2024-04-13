from django.db import models
from db_connection import db

# Create your models here.
online_orders_data = db['online_orders']
products_data = db['products']