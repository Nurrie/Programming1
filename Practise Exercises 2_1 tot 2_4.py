#Opdracht 2_1: schrijf een programma dat een nieuwe lijst maakt (en print) met het aantal voorkomens van de letters in alfabetische volgorde.
letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
letters.count('A')
letters.count('B')
letters.count('C')
letters2=[letters.count('A'), letters.count('B'), letters.count('C')]
print(letters2)

#Opdracht 2_2: De Hogeschool Utrecht wil studenten financieel ondersteunen bij hun studie, afhankelijk van de cijfers die een student haalt. Voor elk cijferpunt krijg je € 30,-. Voor een 1,0 krijgt je dus 30 euro, voor een 2,5 krijgt je 75 euro en voor een 10,0 beloont de HU een student met € 300,-.
#Maak variabelen cijferICOR, cijferPROG en cijferCSN. Geef ze alle drie de waarde die jij verwacht dat je voor de betreffende vakken in blok 1 zult gaan halen.
cijferICOR=8
cijferPROG=7
cijferCSN=6

# Maak nu vervolgens ook de volgende variabelen aan (gemiddeled beloning, overzicht; en bereken de bijbehorende waarden.
gemiddelde=(cijferICOR+cijferPROG+cijferCSN)/3
print(gemiddelde)
cijfer_totaal=cijferICOR+cijferPROG+cijferCSN
print(cijfer_totaal)
beloning=cijfer_totaal*30
print(beloning)
overzicht='Mijn cijfers (gemiddeld een 7.0) leveren een beloning van €630.0 op!'
print(overzicht)

#Opdracht 2_3: Voeg haakjes toe aan de volgende expressies zodat ze naar True evalueren.
0==(1==2)
print(0==(1==2))
2+(3==4)+5==7
print(2+(3==4)+5==7)
1<-1==3>4
print((1<-1)==(3>4))

#Opdracht 2_4:Schrijf een programma dat de gebruiker vraagt om zijn uurloon, het aantal uur dat hij of zij gewerkt heeft en dat daarna het salaris uitprint.
uurloon=8.0
uren_gewerkt=20

uurloon=int(input('Wat verdien je per uur?'))
print(uurloon)
uren_gewerkt=int(input('Hoeveel uur heb je gewerkt?'))
print(uren_gewerkt)

#per uur wordt er €8.0 verdient. Er is 20 uur gewerkt.
salaris=(uren_gewerkt*uurloon)
print(salaris)
