from classes.tests._MongodbConnectieCheck import *
from classes._data_recieve import Getdata
from classes._data_converter import Converter
from classes._data_sender import DataSender
from classes._sql_aanmaken import CreateDatabase

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["huwebshop"]

databaseData = Getdata(myclient=myclient, mydb=mydb)

# print('first product name and price: ', databaseData.first_name_price())

# print('first product name of desired letter: ', databaseData.name_start_letter(letter='R'))

# print('average price of all products: ', databaseData.average_price())

convert = Converter(mydb, myclient)
sender = DataSender()
create = CreateDatabase()
create.drop_create()
# cts(file='products.csv')

# convert.products(['_id', 'name', 'brand', 'category', 'deeplink', 'fast_mover', 'gender', 'herhaalaankopen', 'price.selling_price'])
# convert.visitors(['recommendations.latest_visit'])
# convert.sessions(['buid', 'user_agent.identifier', 'session_start', 'session_end'])

sender.send_products(file='functions/products.csv')
sender.send_visitors(file='functions/visitors.csv')
sender.send_sessions(file='functions/sessions.csv')
