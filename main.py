import pymongo
import psycopg2

from classes.tests._MongodbConnectieCheck import *
from classes._data_recieve import Getdata
from classes._data_converter import Converter

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["huwebshop"]

databaseData = Getdata(myclient=myclient, mydb=mydb)

print('first product name and price: ', databaseData.first_name_price())

print('first product name of desired letter: ', databaseData.name_start_letter(letter='R'))

print('average price of all products: ', databaseData.average_price())

convert = Converter(mydb, myclient)

convert.products(['_id', 'price.selling_price'])
# convert.visitors(['_id', 'buids', 'recommendations'])
# convert.sessions(['_id', 'user_agent', 'segment'])
