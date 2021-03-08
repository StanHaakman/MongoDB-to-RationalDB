import pandas as pd
import numpy as np

# Pandas DataFrame volledig weergeven.
pd.set_option('display.max_rows', None, 'display.max_columns', None,
              'display.width', None, 'display.max_colwidth', None)
# Pandas DataFrame wetenschappelijke notatie onderdrukken.
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# middels nrows bepaal je hoeveel elementen je inlaadt sinds de dataset erg groot is.
df = pd.read_csv('sessions.csv', nrows=10)

# loop door alle buid en strp de eetste twee en laatste twee karakters.
# plaats resultaat in een nieuwe lijst
df_lijst = list(df.buid)  # bepaal hoeveel rijen je wil inlezen
buid = np.array([])
for value in df_lijst:
    value = value[2:-2]
    buid = np.append(buid, value)

# pas nieuwe lijst aan in de dataframe en sla deze wijzigingen op.
df['buid'] = buid
df.to_csv('sessions.csv', index=False)

print(df.head())  # weergeef de eerste vijf elementen van de dataframe.
