import psycopg2


def connect_to_db():
    con = psycopg2.connect(host='localhost', database='huwebshop', user='postgres', password='postgres')

    return con


def get_data(con, sqlstring):
    cursor = con.cursor()

    cursor.execute(sqlstring)

    record = cursor.fetchone()

    return record


print(get_data(connect_to_db(), 'SELECT version()'))
