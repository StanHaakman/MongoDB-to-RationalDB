from pymongo import MongoClient


def mongodb_connectie_check():
    """Connectie tussen Python en MongoDB controleren.
    returnt een lijst met alle beschikbare databases"""
    myclient = MongoClient("mongodb://localhost:27017/")  # python verbinden met MongoDB localhost
    return myclient.list_database_names()


print(mongodb_connectie_check())
