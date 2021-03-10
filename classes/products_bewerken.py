import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None, 'display.max_columns', None,
              'display.width', None, 'display.max_colwidth', None)
# Pandas DataFrame wetenschappelijke notatie onderdrukken.
pd.set_option('display.float_format', lambda x: '%.3f' % x)

df = pd.read_csv('products.csv', encoding='utf-8')
# print(df.columns)  # lijst van alle originele kolomnamen
print('Dataset ingeladen en wordt bewerkt.')

kolommen = ['brand', 'category', 'color', 'gender', 'doelgroep', 'soort', 'variant',
            'sub_category', 'sub_sub_category']
for kolom in kolommen:
    df[kolom] = df[kolom].replace(np.nan, 'onbekend', regex=True)

df['color'] = df['color'].where(df['color'] != 'Gezin', 'onbekend')
df['color'] = df['color'].where(df['color'] != '4005808639892', 'onbekend')

vals_lijst = ['Gezin', 'B2B', 'Kinderen', 'Senior', 'Baby', 'Grootverpakking', '8719497835768']
for vals in vals_lijst:
    df['gender'] = df['gender'].where(df['gender'] != vals, 'onbekend')

df['herhaalaankopen'] = df['herhaalaankopen'].replace(np.nan, False, regex=True)

df['doelgroep'] = df['doelgroep'].where(df['doelgroep'] != 'Geen', 'onbekend')
df['doelgroep'] = df['doelgroep'].where(df['doelgroep'] != 'Kantoor', 'kantoor')
df['doelgroep'] = df['doelgroep'].where(df['doelgroep'] != 'volwassene', 'Volwassenen')

df.columns = ['product_id', 'merk', 'categorie', 'kleur', 'geslacht', 'herhaalaankopen',
              'naam', 'prijs', 'doelgroep', 'soort', 'variant',
              'sub_categorie', 'sub_sub_categorie']  # bepaal kolomnamen en volgorde

print(df.isna().sum())
print(df.sample(10))

df.to_csv('products.csv', index=False)  # opslaan naar csv
print('processen beeindigd en opgeslagen!')
