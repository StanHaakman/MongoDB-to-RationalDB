import math
import pandas as pd
import numpy as np


def id_filter(dataframe):
    id = dataframe[['_id']]  # selecteer gewenste kolomnaam
    id_lijst = list(id._id)  # zet om naar een lijst
    id_verbeterd = []
    for value in id_lijst:
        value = ''.join(filter(str.isdigit, str(value)))  # hier strippen
        id_verbeterd.append(value)
    dataframe._id = id_verbeterd  # pas kolom aan in data dataframe
    return dataframe


def id_datatype_nan(dataframe):
    # zowel de datatype als nan wordt verholpen in deze fucntie
    id_verbeterd = []
    for value in dataframe['_id']:
        if math.isnan(value):
            value = -1.0  # nan omzetten naar -1
        id_verbeterd.append(int(value))  # alle waardes omzetten naar integer
    dataframe._id = id_verbeterd  # pas kolom aan in data dataframe
    return dataframe


def id_duplicates(dataframe):
    c = 0
    d = 0
    id_verbeterd = []
    for value in dataframe['_id']:
        if value not in id_verbeterd:
            id_verbeterd.append(value)
        else:
            d += 1
            while True:
                if c in id_verbeterd:
                    c += 1
                else:
                    break
            id_verbeterd.append(c)
    print(c, d)
    return dataframe


def id_informatie(dataframe):
    print()
    print(dataframe.isna().sum())
    print()
    print(dataframe.info())
    print()
    return dataframe


# STAP 1
df = pd.read_csv('products.csv', encoding='latin-1')
# print(df.columns)  # weergeef alle kolomnamen
df.columns = ['_id', 'selling_price', 'name', 'brand', 'category', 'deeplink',
              'fast_mover', 'gender', 'herhaalaankopen']  # bepaal kolomnamen

print('aanpassingen gestart, momentje!')
df = id_filter(df)
df.to_csv('products.csv', index=False)

# STAP 2
df = pd.read_csv('products.csv', encoding='latin-1')
df = id_datatype_nan(df)
df = id_duplicates(df)

# STAP 3
id_informatie(df)
print(type(df))
df.to_csv('products.csv', index=False)
print('processen beeindigd en opgeslagen!')
