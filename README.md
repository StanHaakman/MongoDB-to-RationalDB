# MongoDB-to-RationalDB
Het uitpuzzelen van het aan elkaar knopen van technologie is typisch iets dat beter gaat in samenwerking en weinig creatieve elementen heeft om je individuele input in te geven.

We hebben voor een verdere uitleg van het project een losse pagina, die kan je hier vinden:
https://stanhaakman.github.io/MongoDB-to-RationalDB/

Hier geven we verder verdieping over de volgende onderdelen:
<ul>
  <li>Samenvatting;</li>
  <li>Resultaten tussenopdrachten;</li>
    <ul>
      <li>Opdracht 2a;</li>
      <li>Opdracht 2b;</li>
      <li>Opdracht 2c;</li>
    </ul>
  <li>Gebruikte technieken</li>
  <li>Onderbouwing van gekozen oplossing</li>
  <li>Belangrijke codeblokken</li>
  <li>OOP (Objectgeoriënteerd programmeren)</li>
  <li>Indeling project</li>
</ul>

## Installatie instructies
Hier volgt een visuele en textuele uitleg over een nieuwe gebruiker dit project werkend krijgt.

### Prerequirements
Voordat dit project werkt zijn er een aantal onderdelen nodig die zijn hier te vinden.

<ul>
  <li>MongoDB moet geinstalleerd zijn</li>
  <ul>
    <li>Met MongoImport moet de goede database aanwezig zijn. Deze bevat gevoelige gegevens dus hier gaan we verder niet op in in dit document.</li>
  </ul>
  <li>Python Libraries: Deze kan je vooraf globaal installeren of met het opstellen van het project local geinstalleren.
    <ul>
      <li>pymongo library</li>
      <li>psycopg2</li>
      <li>csv</li>
    </ul>
  </li>
  <li>Postgress</li>
  <li>Python</li>
</ul>

### Setup

Download een zip bestand van de data of kies ervoor om de git te Forken naar je eigen account en dan clonen.

Zorg dat alle benodigde libraries gedownload anders kan installeren met:
```
python3 install pymongo

&&

python3 install psycopg2

&&

python3 install csv
```

Voordat het programma werkt moet er een file aangemaakt worden genaamd: dbsecret.py

Geef in deze file de volgende onderdelen aan en verander de inhoud naar jou eigen postgress gegevens:
```
user = 'user'
database = 'dbname'
password = 'password'
```

Open het project folder in de terminal en run dit commando:

```
python3 main.py
```
