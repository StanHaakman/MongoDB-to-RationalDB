import pandas as pd

# Pandas DataFrame volledig weergeven.
pd.set_option('display.max_rows', None, 'display.max_columns', None,
              'display.width', None, 'display.max_colwidth', None)
# Pandas DataFrame wetenschappelijke notatie onderdrukken.
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# middels nrows bepaal je hoeveel elementen je inlaadt sinds de dataset erg groot is.
df = pd.read_csv('sessions.csv')
print('dataset ingeladen')

buid = df['buid'].squeeze()  # zet dataframe om naar series
buid = buid.str.strip("[']")
print('series met buids aangemaakt')

# pas nieuwe lijst aan in de dataframe en sla deze wijzigingen op.
df['buid'] = buid
print('buid toegepast op de dataframe. wordt nu opgeslagen')
df.to_csv('sessions.csv', index=False)
print('nieuwe dataframe in csv verwerkt!')

print(df.head())  # weergeef de eerste vijf elementen van de dataframe.