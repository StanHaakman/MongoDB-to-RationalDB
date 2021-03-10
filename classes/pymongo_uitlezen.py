import csv
import pymongo


class Pymongo:

    def __init__(self):
        self.client = pymongo.MongoClient("localhost", 27017)
        self.database = self.client["huwebshop"]

    @staticmethod
    def convert_to_csv(fieldnames, filename, dbtable):
        with open(filename, 'w', newline='', encoding='UTF-8') as csvout:
            writer = csv.DictWriter(csvout, fieldnames=[i if '.' not in i else i.split('.', 1)[1] for i in fieldnames])
            writer.writeheader()
            content = dbtable.find()
            c = 0
            for item in content:
                # noinspection PyBroadException
                try:
                    writer.writerow(
                        {
                            i if '.' not in i else i.split('.', 1)[1]: item.get(i) if '.' not in i else
                            item.get(i.split('.', 1)[0])[i.split('.', 1)[1]]
                            for i in fieldnames
                        }
                    )
                except:
                    continue
                c += 1
                if c % 10000 == 0:
                    print('{} product records written...'.format(c))
        print('Finished creating the product database content')

    def products(self, fieldnames):
        filename = 'products.csv'
        dbtable = self.database.products
        self.convert_to_csv(fieldnames, filename, dbtable)

    def visitors(self, fieldnames):
        filename = 'visitors.csv'
        dbtable = self.database.visitors
        self.convert_to_csv(fieldnames, filename, dbtable)

    def sessions(self, fieldnames):
        filename = 'sessions.csv'
        dbtable = self.database.sessions
        self.convert_to_csv(fieldnames, filename, dbtable)
