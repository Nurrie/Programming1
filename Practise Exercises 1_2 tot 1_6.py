# Opdracht 1_2
#Hoeveel letters zijn er in 'Supercalifragilisticexpialidocious'?
s='Supercalifragilisticexpialidocious'
print(len('Supercalifragilisticexpialidocious'))
#Komt in 'Supercalifragilisticexpialidocious' de tekst 'ice' voor?
print('ice' in 'Supercalifragilisticexpialidocious')
#Is het woord 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?
print('Antidisestablishmentarianism'>'Honorificabilitudinitatibus')
#Welke componist komt in alfabetische volgorde het eerst: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'? Welke het laatst?
componist=['Berlioz', 'Borodin', 'Brian','Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
print(componist)
componist.sort()
print(componist)

#Opdracht 1_3
#Ken de waarde 6 toe aan variabele a, en waarde 7 aan variabele b
a=6
b=7
#Ken aan variabele c als waarde het gemiddelde van a en b toe.
c=(a+b)/2
print((a+b)/2)
#Ken aan variabele inventaris de een lijst van strings toe: ‘papier’, ‘nietjes’, en ‘pennen’.
inventaris=['papier', 'nietjes', 'pennen']
#Ken aan variabelen voornaam, tussenvoegsel en achternaam je eigen naamgegevens toe.
voornaam='nur'
achternaam='batur'
#Ken aan variabele mijnnaam de variabelen van opdracht 4 (met spaties er tussen) toe.
mijnnaam=voornaam+' '+achternaam
print(mijnnaam)

#6.75 groter is dan a en kleiner b.
6.75 > a and 6.75 < b
print(6.75 > a and 6.75 < b)

#Is de lengte van inventaris meer dan 5 keer zo groot als de lengte van variabele mijnnaam?
print(len(inventaris)>5*len(mijnnaam))

#de lijst inventaris leeg is, of juist meer dan 10 items bevat.


#een nieuwe list met 1 artiest aan te maken met de naam favorieten.
favorieten=['artiest1']
print(favorieten)
#de lijst uit te breiden met een tweede artiest.
favorieten.append('artiest2')
print(favorieten)
#de tweede artiest te vervangen door een andere naam.
favorieten[1]='artiest3'
print(favorieten)

list=[3,7,-2, 12]
print(max(list)-min(list))
