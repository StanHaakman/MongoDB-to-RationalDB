import psycopg2
import csv



class DataSender:


    def __init__(self):
        pass

    def openconnection(self):
        con = psycopg2.connect(
            host='localhost',  # De host waarop je database runt
            database='huwebshop',  # Database naam
            user='postgres',  # Als wat voor gebruiker je connect, standaard postgres als je niets veranderd
            password='Elvis&Presley'  # Wachtwoord die je opgaf bij installatie
            # port=5432 runt standaard op deze port en is alleen nodig als je de port handmatig veranderd
        )
        return con

    def send_products(self, file):
        con = self.openconnection()
        cur = con.cursor()
        with open(file, 'r', encoding="utf-8") as csvf:
            reader = csv.reader(csvf)
            next(reader)
            for row in reader:
                cur.execute("insert into products (idproducts, name, brand, category, deeplink, fastmover, target, herhaalaankopen, price) "
                            "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)",(row))
        con.commit()
        print("Products is now done")

    def send_sessions(self, file):
        con = self.openconnection()
        cur = con.cursor()
        with open(file, 'r') as csvf:
            reader = csv.reader(csvf)
            next(reader)
            for row in reader:
                cur.execute("insert into Sessions (buids_buids, identifier, sessie_start, sessie_end) "
                            "values (%s, %s, %s, %s)",(row))
        con.commit()
        print("Sessions is now done")

    def send_visitors(self, file):
        '''

        :param file:
        :return:
        '''
        con = self.openconnection()
        cur = con.cursor()
        with open(file, 'r', encoding="utf-8") as csvf:
            reader = csv.reader(csvf)
            next(reader)
            for row in reader:
                cur.execute("insert into Visitors (latest_visit) "
                            "values (%s)",(row))
        con.commit()
        print("Visitors is now done")