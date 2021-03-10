import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None, 'display.max_columns', None,
              'display.width', None, 'display.max_colwidth', None)
# Pandas DataFrame wetenschappelijke notatie onderdrukken.
pd.set_option('display.float_format', lambda x: '%.3f' % x)

df = pd.read_csv('products.csv', encoding='utf-8')
# print(df.columns)  # lijst van alle originele kolomnamen
df.columns = ['_id', 'brand', 'category', 'color', 'gender', 'herhaalaankopen',
              'name', 'selling_price', 'doelgroep', 'soort', 'variant',
              'sub_category', 'sub_sub_category']  # bepaal kolomnamen en volgorde
print('Dataset ingeladen en wordt bewerkt.')

kolommen = ['brand', 'category', 'color', 'gender', 'doelgroep', 'soort', 'variant',
            'sub_category', 'sub_sub_category']
for kolom in kolommen:
    df[kolom] = df[kolom].replace(np.nan, 'onbekend', regex=True)

df['color'] = df['color'].where(df['color'] != 'Gezin', 'onbekend')
df['color'] = df['color'].where(df['color'] != '4005808639892', 'onbekend')

df['gender'] = df['gender'].where(df['gender'] != 'Gezin', 'onbekend')
df['gender'] = df['gender'].where(df['gender'] != 'B2B', 'onbekend')
df['gender'] = df['gender'].where(df['gender'] != 'Kinderen', 'onbekend')
df['gender'] = df['gender'].where(df['gender'] != 'Senior', 'onbekend')
df['gender'] = df['gender'].where(df['gender'] != 'Baby', 'onbekend')
df['gender'] = df['gender'].where(df['gender'] != 'Grootverpakking', 'onbekend')
df['gender'] = df['gender'].where(df['gender'] != '8719497835768', 'onbekend')

df['herhaalaankopen'] = df['herhaalaankopen'].replace(np.nan, False, regex=True)

df['doelgroep'] = df['doelgroep'].where(df['doelgroep'] != 'Geen', 'onbekend')
df['doelgroep'] = df['doelgroep'].where(df['doelgroep'] != 'Kantoor', 'kantoor')
df['doelgroep'] = df['doelgroep'].where(df['doelgroep'] != 'volwassene', 'Volwassenen')

print(df.isna().sum())
print(df.sample(10))

df.to_csv('products.csv', index=False)  # opslaan naar csv
print('processen beeindigd en opgeslagen!')
