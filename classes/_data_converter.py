import pymongo
from pymongo import MongoClient
import csv


class Converter:

    def __init__(self, mydb, myclient):
        self.myclient = myclient
        self.mydb = mydb

    def convert_to_csv(self, fieldnames, filename, dbtable):
        with open(filename, 'w', newline='') as csvout:
            writer = csv.DictWriter(csvout, fieldnames=fieldnames)
            writer.writeheader()
            c = 0
            for item in dbtable.find():
                try:
                    writer.writerow({i: item.get(i) for i in fieldnames})
                except:
                    continue
                c += 1
                if c % 10000 == 0:
                    print('{} product records written...'.format(c))
        print('Finished creating the product database content')

    def products(self, fieldnames):
        filename = 'products.csv'
        dbtable = self.mydb.products
        self.convert_to_csv(fieldnames, filename, dbtable)

    def visitors(self, fieldnames):
        filename = 'visitors.csv'
        dbtable = self.mydb.visitors
        self.convert_to_csv(fieldnames, filename, dbtable)

    def sessions(self, fieldnames):
        filename = 'sessions.csv'
        dbtable = self.mydb.sessions
        self.convert_to_csv(fieldnames, filename, dbtable)
