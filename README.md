# Thema van de API: Muziekcollectie Beheer

Deze API stelt gebruikers in staat om een digitale catalogus van cd's bij te houden. De gebruikers kunnen informatie over artiesten en cd's toevoegen, bekijken en verwijderen. Daarnaast is het mogelijk om beoordelingen (reviews) en commentaren over individuele cd's toe te voegen en te raadplegen.

## Belangrijkste Functionaliteiten:

### Artiesten Beheer:

#### Toevoegen van Artiesten:

Gebruikers kunnen nieuwe artiesten aan de database toevoegen door hun naam, genre en andere relevante details op te geven.

#### Bekijken van Artiesten:

De API biedt mogelijkheden om een lijst van alle artiesten te bekijken of om specifieke artiesten op te zoeken.

#### Verwijderen van Artiesten:

Artiesten kunnen uit de database worden verwijderd. Dit proces zorgt ervoor dat alle gerelateerde cd's en reviews ook verwijderd worden om integriteit van de data te behouden.

### CD's Beheer:

#### Toevoegen van CD's:

Gebruikers kunnen nieuwe cd's aan de catalogus toevoegen met details zoals titel, releasejaar, en de gekoppelde artiest.

#### Bekijken van CD's:

Er is een mogelijkheid om alle cd's te bekijken, of om te zoeken naar een cd op titel of via de unieke ID.

#### Verwijderen van CD's:

Wanneer een cd wordt verwijderd, worden ook automatisch de gekoppelde reviews verwijderd.

### Reviews Beheer:

#### Toevoegen van Reviews:

Gebruikers kunnen beoordelingen toevoegen aan een cd door een rating en commentaar op te geven, samen met de ID van de cd.

#### Bekijken van Reviews:

Reviews kunnen per cd bekeken worden.

## Conclusie

De API is zo ontworpen dat het eenvoudig is voor gebruikers om de informatie te beheren via een reeks van HTTP-verzoeken, waardoor het een flexibele tool is voor muziekliefhebbers of verzamelaars. De nadruk ligt op gebruiksgemak en het waarborgen van de integriteit van de gegevens bij elke bewerking.

De link naar mijn eigen gehoste API kan je hier terugvinden:
https://api-arnebogaerts.cloud.okteto.net/docs#/

Onderaan deze set foto's van mijn API, laat ik per endpoint kort zien hoe ze werken, met een korte uitleg.

![Screenshot1](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/34a35dfd-04bc-4840-a997-a64e62e2519a)
![Screenshot2](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/4538aee3-9cb1-4a08-a11e-b701a306e878)
![Screenshot3](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/c69267fe-a570-410d-bef4-58b56171aef1)

## ENDPOINT: GET /cds/

Dit endpoint haalt een lijst van CD's op uit de database. Het is ontworpen om op een handige manier toegang te geven tot de gehele collectie van CD's.

![GET cds](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/fe1b188a-ac33-4813-b93e-10c86fce2a6e)

### Data ophalen:

Bij een GET-verzoek wordt de database gequeryd voor CD's, waarbij de skip en limit parameters worden toegepast, als deze zijn meegegeven. Standaard slaat het 0 records over, en limiteert het resultaat tot 10 CD's. Maar deze waarden kunnen worden aangepast.

### Response:

De response is een lijst van CD's (objecten). Elk van deze objecten bevat details over deze CD, zoals zijn ID, titel en artist.

### Gebruik:

* Om de eerste  10 CD's op te halen: **GET /cds/**
* Om de volgende 10 CD's (d.w.z. CD's 11-20) op te halen: **GET /cds/?skip=10&limit=10**

## ENDPOINT: POST /cds/

Dit endpoint maakt het mogelijk om een nieuwe CD toe te voegen aan de database. Het is bedoeld om de CD-collectie uit te breiden met nieuwe items.

![POST cds](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/35f02cdd-bdfd-4060-8792-e7db80075750)
![POST cds 404](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/4176fdde-2eb6-4701-8061-c71336a719ec)

### Data toevoegen:

* Bij een POST-verzoek ontvangt het endpoint gegevens over een nieuwe CD, waaronder de titel en de naam van de artiest.
* De API zoekt eerst naar de artiest in de database. Als de artiest niet gevonden wordt, geeft het een **404-foutmelding** terug met de melding dat de artiest niet gevonden is.
* Als de artiest wel bestaat, wordt de nieuwe cd aangemaakt en aan de database toegevoegd met de meegegeven titel en de ID van de gevonden artiest.

### Request:

Het POST request moet de volgende gegevens bevatten in JSON-formaat:

* **title**: De titel van de CD.
* **artist_name**: De naam van de artiest van de CD.

### Response:

De response bevat de gegevens van de nieuw toegevoegde CD, inclusief het unieke ID dat door de database is toegekend. Dat wil zeggen de titel van het album en het album ID, alsook de gekoppelde artist met zijn ID.


