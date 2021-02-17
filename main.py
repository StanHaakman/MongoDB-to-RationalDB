import pymongo
from classes.tests._test_importMongodb import *
from classes._data_recieve import getdata

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["huwebshop"]

databaseData = getdata(myclient=myclient, mydb=mydb)

print(databaseData.name_start_letter(letter='R'))
