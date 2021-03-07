import math
import random
import time

import pandas as pd


def id_filteren(dataframe):
    id = dataframe[['_id']]
    id_list = list(id._id)
    id_verbeterd = []
    last_value = int

    for value in id_list:
        waarde = random.randint(0, 9)
        while waarde == last_value:
            waarde = random.randint(0, 9)

        value = str(waarde).join(filter(str.isdigit, str(value)))
        # time.sleep(0.1)
        id_verbeterd.append(value)
        last_value = waarde

    dataframe._id = id_verbeterd

    return dataframe


df = pd.read_csv('visitors.csv', encoding='utf-8')

print('aanpassingen gestart, momentje!')
df = id_filteren(df)


df.to_csv('visitors.csv', index=False)
print('processen beeindigd en opgeslagen!')
