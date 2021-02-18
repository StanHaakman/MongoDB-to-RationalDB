import psycopg2
import dbsecret


def connect_to_db():
    con = psycopg2.connect(host='localhost', database=dbsecret.database, user=dbsecret.user, password=dbsecret.password)

    return con


def get_data(con, sqlstring):
    cursor = con.cursor()

    cursor.execute(sqlstring)

    record = cursor.fetchone()

    return record


print(get_data(connect_to_db(), 'SELECT version()'))
