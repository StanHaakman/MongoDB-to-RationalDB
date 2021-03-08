import pandas as pd


def gender(dataframe):
    """Alle kolomwaarde omzetten naar gewenste waardes.
    Allle nan's worden omgezet naar onbekend."""
    toegestaan = ['Vrouw', 'Man', 'Unisex', 'Gezin', 'B2B', 'Kinderen', 'Senior', 'Baby']
    gender_bewerkt = []
    for value in dataframe['gender']:
        if value not in toegestaan:
            gender_bewerkt.append('onbekend')
        else:
            gender_bewerkt.append(value)
    dataframe['gender'] = gender_bewerkt
    return dataframe


def herhaalaankopen(dataframe):
    """ alle kolomwaarde omzetten naar een boolean.
     Alle nan's worden omgezet naar False."""
    toegestaan = [True, False]
    herhaalnagelopen = []
    for value in dataframe['herhaalaankopen']:
        if value not in toegestaan:
            herhaalnagelopen.append(False)
        else:
            herhaalnagelopen.append(value)

    dataframe['herhaalaankopen'] = herhaalnagelopen
    return dataframe


df = pd.read_csv('products.csv', encoding='utf-8')

print('aanpassingen gestart, momentje!')
df = gender(df)
df = herhaalaankopen(df)

df.to_csv('products.csv', index=False)  # opslaan naar csv
print('processen beeindigd en opgeslagen!')
