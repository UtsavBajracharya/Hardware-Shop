# from pymongo import MongoClient
# import os
# import json

# url = 'mongodb://datastore:27017'
# client = MongoClient(url)
# db = client['hardware_shop']


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ranishstha:o96w9YihM24iYDbG@pythonprojectcluster.a9kbvtb.mongodb.net/?retryWrites=true&w=majority&appName=PythonProjectCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    # Access your database
    db = client.hardware_shop

    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error")
    print(e)


