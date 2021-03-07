import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class CreateDatabase:

    def __init__(self):
        pass

    def drop_create(self):
        try:
            self.drop_database()
        except psycopg2.errors.InvalidCatalogName:
            pass
        self.create_database()
        self.fill_database()
        print("database has been dropped/created/completed")

    def openconnection(self, db=None):
        con = psycopg2.connect(
            host='localhost',  # De host waarop je database runt
            database=db,
            user='postgres',  # Als wat voor gebruiker je connect, standaard postgres als je niets veranderd
            password='postgres'  # Wachtwoord die je opgaf bij installatie
            # port=5432 runt standaard op deze port en is alleen nodig als je de port handmatig veranderd
        )
        return con

    def close_con(self):
        con = self.openconnection()
        cursor = con.cursor()
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        close_con_command = "DROP DATABASE huwebshop;"
        cursor.execute(close_con_command)
        con.commit()
        con.close()

    def drop_database(self):
        con = self.openconnection()
        cursor = con.cursor()
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        drop_table_command = "DROP DATABASE huwebshop;"
        cursor.execute(drop_table_command)
        con.commit()
        print('Database has been dropped')
        con.close()

    def create_database(self):
        con = self.openconnection()
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = con.cursor()
        name = 'huwebshop'
        sqlCreateDatabase = "create database " + name + ";"
        cursor.execute(sqlCreateDatabase)
        con.commit()
        con.close()

    def fill_database(self):
        con = self.openconnection(db='huwebshop')
        cursor = con.cursor()
        with open('huwebshop.sql', 'r') as file:
            content_list = [line.rstrip(';') for line in file]

            tempLst = []
            for i in content_list:
                if i[:2] != '--' and i != '\n':
                    tempLst.append(i[:-1])
            content_list = tempLst

            separator = ' '
            content = separator.join(content_list)
            content_list = content.split(';')

            tempLst = []
            for i in content_list:
                tempLst.append(i + ';')
            tempLst.remove(tempLst[-1])
            content_list = tempLst

            for i in content_list:
                cursor.execute(i)
                con.commit()
            con.close()