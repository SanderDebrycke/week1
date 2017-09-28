print("hello")
print("nog eens hallo ")

#python GEEN declaratie van types
#bv java
#int x = 3
#python ontdekt wel type het is
#Hoe?

x = 3 #int, integer of geheel getal kan ook negatief -3
y = 3.0 #float door het punt
z = "3" #met een string

#commando type
print("x is van het type " + str(type(x)))
print(type(y))
print(type(z))

#naam = input("Tik aub uw naam in")
#print(naam)

print("een tekst met \"quotes\" rond")

#format
#getallen formateren en vraagt minder resources
#zie oefening 3

#Oefening 1
print("Sander")
print("Debrycke")
print("sanderdebrycke@hotmail.com")

#Oefening 2
print("Labo Basic Programming,\n \t Labo week 1 \n \t \t Kennis making met \"Python\",\n \t \t Werken met variabelen.")
print("Labo Basic Programming")
print("\t Labo week 2")

#Oefening 3
naam = "Sander"
voornaam = "Debrycke"
leeftijd = "19"
print("Voornaam is : {0} naam is : {1} en leeftijd is {2}".format(voornaam,naam,leeftijd))

#Oefening 4
#Variabelen
a = 1
b = 2
#Decimaal
print(a , b)
#Octaal
print(oct(a),oct(b))
#Hexadecimaal
print(hex(a), hex(b))
#Binair
print(bin(a), bin(b))
#Som
c = a + b
print(c)

#Oefening 5
Basis ="1.6"
Hoogte = "2.1"
Oppervlakte = Basis + Hoogte

print("Geef de basis van de driehoek op: ", Basis)
print()


