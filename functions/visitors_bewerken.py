import math
import pandas as pd


def id_filteren(dataframe):
    id = dataframe[['_id']]
    id_list = list(id._id)
    id_verbeterd = []

    for value in id_list:
        value = ''.join(filter(str.isdigit, str(value)))
        id_verbeterd.append(value)

    dataframe._id = id_verbeterd

    return dataframe


def id_duplicates_old(dataframe):
    c, d = 0, 0
    id_verbeterd = []
    for value in dataframe['_id']:
        if value not in id_verbeterd:
            id_verbeterd.append(value)
        else:
            d += 1
            while True:
                if c % 10000 == 1:
                    print(f'{c} punten verwerkt')
                if c in id_verbeterd:
                    c += 1
                    # print(f'nu {c}')
                else:
                    break
            c += 1
            id_verbeterd.append(c)
    print(c, d)
    return dataframe


def id_duplicates(dataframe):
    dataframe.drop_duplicates(subset=['_id'], keep='first', inplace=False)
    return dataframe


df = pd.read_csv('visitors.csv', encoding='utf-8')

print('aanpassingen gestart, momentje!')
df = id_filteren(df)

# print(len(df.duplicated(subset=['_id'])))

df = id_duplicates_old(df)

df.to_csv('visitors.csv', index=False)
print('processen beeindigd en opgeslagen!')
