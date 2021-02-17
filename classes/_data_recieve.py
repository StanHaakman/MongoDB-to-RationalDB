from pymongo import MongoClient


class getdata(object):
    """
    Deze class is gemaakt voor het ophalen van data
    geef een uitleg van elke functie in de vorm van een comment
    """

    def __init__(self, myclient, mydb):
        self.myclient = myclient
        self.mydb = mydb

    def first_name_price(self):
        # Geef de naam en de prijs van het eerste product in de lijst
        return self.mydb.products.find_one({}, {"_id": 0, "name": 1, "price.selling_price": 1})['name']

    def name_start_letter(self, letter):
        # Geef het eerste product terug, waar de naam begint met het gewenste letter
        for i in self.mydb.products.find({}, {"_id": 0, "name": 1}):
            var = i['name']
            if letter == var[0]:
                return var

    def average_price(self):
        totalprice = 0
        totalitems = 0

        for i in self.mydb.products.find({}, {"_id": 0, "price.selling_price": 1}):
            if i != {}:
                var = i["price"]
                newvar = var["selling_price"]

                # Pijzen die 0 zijn ook meenemen of overslaan.
                if newvar != 0:
                    totalprice += newvar
                    totalitems += 1

        return totalprice / totalitems
