import pymongo
import psycopg2

from classes.tests._test_importMongodb import *
from classes._data_recieve import Getdata

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["huwebshop"]

databaseData = Getdata(myclient=myclient, mydb=mydb)

print('first name: ', databaseData.first_name_price())

print('first product name of desired letter: ', databaseData.name_start_letter(letter='R'))

print('average price of all products: ', databaseData.average_price())

