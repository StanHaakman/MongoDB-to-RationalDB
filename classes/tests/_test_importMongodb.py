from pymongo import MongoClient


def test_mongoDB():
    # Met deze testfile kun je testen of je MongoDB goed werkt.
    myclient = MongoClient("mongodb://localhost:27017/")
    print(myclient.list_database_names())  # Middels deze printstatement kan je controleren of de database correct is geimporteerd
    mydb = myclient["huwebshop"]