import psycopg2

class CreateDatabase:

    def __init__(self):
        pass

    def drop_create(self):
        self.drop_database()
        self.create_database()
        self.fill_database()
        print("database created")

    def openconnection(self):
        con = psycopg2.connect(
            host='localhost',  # De host waarop je database runt
            database='huwebshop',  # Database naam
            user='postgres',  # Als wat voor gebruiker je connect, standaard postgres als je niets veranderd
            password='Elvis&Presley'  # Wachtwoord die je opgaf bij installatie
            # port=5432 runt standaard op deze port en is alleen nodig als je de port handmatig veranderd
        )
        return con

    def drop_database(self):
        con = self.openconnection()
        cursor = con.cursor()
        drop_table_command = "DROP DATABASE huwebshop"
        cursor.execute(drop_table_command)
        con.commit()

    def create_database(self):
        con = self.openconnection()
        cursor = con.cursor()
        create_database_command = "CREATE DATABASE huwebshop"
        cursor.execute(create_database_command)
        con.commit()

    def fill_database(self):
        con = self.openconnection()
        cursor = con.cursor()
        with open('huwebshop.sql', 'r') as file:
            lines = file.readlines()
        cursor.execute(lines)
        con.commit()
