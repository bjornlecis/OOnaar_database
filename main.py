class Cursist:
    def __init__(self,id,voornaam,achternaam):
        self.id = id
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.cursussen = []

    def __str__(self):
        return "ID: {} voornaam {} achternaam {}".format(self.id,self.voornaam,self.achternaam)
    def voeg_cursus_toe(self,cursus):
        self.cursussen.append(cursus)

class Docent:
    def __init__(self,id,naam, uurprijs):
        self.id = id
        self.naam = naam
        self.uurprijs = uurprijs

    def __str__(self):
        return "ID: {} Naam: {} uurprijs {}".format(self.id,self.naam, self.uurprijs)


class Cursus:
    def __init__(self,id,naam,aantal_uur, docent):
        self.id = id
        self.naam = naam
        self.aantal_uur = aantal_uur
        self.docent = docent

    def __str__(self):
        return "ID {} Naam: {} aantal uur: {}\t\t Docent: {}".format(self.id,self.naam,self.aantal_uur,self.docent.naam)



def toon_cursist_cursus():
    for x in Lijst_cursist:
        print(x.voornaam+" "+x.achternaam)
        for y in x.cursussen:
            print(y)

def toon_docenten():
    for x in Lijst_docent:
        print(x)

def sorteer_cursist_voornaam():
    Lijst_cursist.sort(key= lambda x:x.voornaam)
    for x in Lijst_cursist:
        print(x)

def voeg_cursus_toe():
    docent_id = input("wie zal deze cursus geven, geef het id")
    for x in Lijst_docent:
        if docent_id == x.id:
            d = Docent(x.id,x.naam,x.uurprijs)

    cursus_id = input("geef het id van de cursus")
    cursus_naam = input("geef de naam van de cursus")
    aantal_uren = int(input("geef het aantal uren in"))
    c = Cursus(cursus_id,cursus_naam,aantal_uren,d)
    Lijst_cursus.append(c)

def voeg_cursus_toe_aan_cursist():
    cursus_id = input("geef id van cursus")
    for x in Lijst_cursus:
        if x.id == cursus_id:
            c = Cursus(x.id,x.naam,x.aantal_uur,x.docent)
    cursist_id = input("geef het id van cursist")
    for y in Lijst_cursist:
        if y.id == cursist_id:
            y.voeg_cursus_toe(c)



d1 = Docent("D1","Jansen",50)
d2 = Docent("D2","Peeters",60)
CU1 = Cursus("CUR1","Python deel 1",20,d1)
CU2 = Cursus("CUR2","Python deel 2",30,d2)
CU3 = Cursus("CUR3","Python Panda",16,d2)
S1 = Cursist("ST1","Bert","Jansen")
S2 = Cursist("ST2","Karel","Vanhees")
S3 = Cursist("ST3","Anja","Peters")
S1.voeg_cursus_toe(CU1)
S2.voeg_cursus_toe(CU1)
S2.voeg_cursus_toe(CU2)
S2.voeg_cursus_toe(CU3)

Lijst_cursus = [CU1,CU2,CU3]
Lijst_cursist = [S1,S2,S3]
Lijst_docent = [d1,d2]

#optie 1 toon_cursist_cursus()
#optie 2 toon_docenten()
#optie 3 sorteer_cursist_voornaam()
#optie 4 voeg_cursus_toe()
voeg_cursus_toe_aan_cursist()
toon_cursist_cursus()




