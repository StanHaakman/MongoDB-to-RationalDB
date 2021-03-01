import pymongo
from pymongo import MongoClient
import csv

# myclient = MongoClient("mongodb://localhost:27017/")
# mydb = myclient["huwebshop"]


def foo():

    with open ('products.csv', 'w', newline='') as csvout:
        fieldnames = ['id', 'brand', 'name']
        writer = csv.DictWriter(csvout, fieldnames=fieldnames)
        writer.writeheader()
        c = 0
        for product in mydb.products.find():
            try:
                if product['price']['selling_price'] != 0:
                    writer.writerow({'id': product["_id"],
                                     'brand': product.get('brand', None),
                                     'name': product.get('name', None)})
            except:
                continue
            c += 1
            if c % 10000 == 0:
                print('{} product records written...'.format(c))
    print('Finished creating the product database content')


class Converter:

    def __init__(self, mydb, myclient):
        self.myclient = myclient
        self.mydb = mydb

    def convert_to_csv(self):
        pass

    def products(self):
        pass

    def visitors(self):
        pass

    def sessions(self):
        pass
