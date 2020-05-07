import pymongo
from pymongo import MongoClient
cluster = MongoClient('mongodb+srv://bigpapaasg:ohyeah?@cluster0-0hiha.mongodb.net/test?retryWrites=true&w=majority')
db = cluster["test"]
collection = db["test"]
post = {
    "_id":0,"name":"papa","score":5
}
collection.insert_one(post)
