import math
import random

import pandas as pd
# import numpy as np


def id_filter(dataframe):
    id = dataframe[['_id']]  # selecteer gewenste kolomnaam
    id_lijst = list(id._id)  # zet om naar een lijst
    id_verbeterd = []
    last_value = int

    for value in id_lijst:
        waarde = random.randint(0, 9)
        while waarde == last_value:
            waarde = random.randint(0, 9)

        value = str(waarde).join(filter(str.isdigit, str(value)))
        id_verbeterd.append(value)
        last_value = waarde

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
    c, d = 0, 0
    id_verbeterd = []
    for value in dataframe['_id']:
        if value not in id_verbeterd:
            id_verbeterd.append(value)
        else:
            d += 1
            while True:
                if c % 100 == 1:
                    print(f'{c} punten verwerkt')
                if c in id_verbeterd:
                    c += 1
                    print(f'nu {c}')
                else:
                    break
            c += 1
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
df = pd.read_csv('products.csv', encoding='utf-8')
# print(df.columns)  # weergeef alle kolomnamen
df.columns = ['_id', 'selling_price', 'name', 'brand', 'category', 'deeplink',
              'fast_mover', 'gender', 'herhaalaankopen']  # bepaal kolomnamen

print('aanpassingen gestart, momentje!')
df = id_filter(df)
df.to_csv('products.csv', index=False)

# STAP 2
df = pd.read_csv('products.csv', encoding='utf-8')
df = id_datatype_nan(df)
df = id_duplicates(df)

# STAP 3
id_informatie(df)
print(type(df))
df.to_csv('products.csv', index=False)
print('processen beeindigd en opgeslagen!')
