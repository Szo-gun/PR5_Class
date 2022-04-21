from cgi import test
from re import I
from turtle import color
from faker import Faker
fake = Faker()

###JAK ZROBIĆ ABY ARGUMENTY BYŁY OPCJONALNE?!

class event:
    def __init__(self, imie, nazwisko, mail):
    #def __init__(self, imie, nazwisko, firma, stanowisko, mail):
        self.imie =  imie
        self.nazwisko = nazwisko
        #self.firma = firma
        #self.stanowisko = stanowisko
        self.mail = mail
        #Variables:
        self._imie_len = 0
        self._nazwisko_len = 0 
    def __repr__(self):
       #return f"{self.imie} {self.nazwisko}, {self.firma}, {self.stanowisko}, {self.mail}"
        return f"{self.imie} {self.nazwisko}, {self.mail}"

    def imie_len(self):
        return self._imie_len
    def imie_len(self):
         print(f"Imię {person.imie} ma {len(person.imie)} znaków")

    def nazwisko_len(self):
        return self._nazwisko_len
    def nazwisko_len(self):
        print(f"Nazwisko {person.nazwisko} ma {len(person.nazwisko)} znaków"  + "\n")

    def contact(self):
        print(f"Kontaktuję się z: {person}")

def dane(name):
    #return(name.imie, name.nazwisko, name.firma, name.stanowisko, name.mail)
    return(name.imie, name.nazwisko, name.mail)

# Pętla generująca 5 losowych wizytówek
for i in range(0,5):
    #person = event(imie=fake.first_name(), nazwisko=fake.last_name(), firma=fake.company(), stanowisko=fake.job(), mail=fake.email() + "\n")
    person = event(imie=fake.first_name(), nazwisko=fake.last_name(), mail=fake.email())
    dane(person) 
    globals()["Nowy%s" % i] = person
    event.contact(person)
    event.imie_len(person.imie)
    event.nazwisko_len(person.imie)

# Użycie metody contact - wyświetlającej zapis: "Kontaktuję się z {}"


# Lista z wygenerowanymi kontaktami    
Wszyscy = [Nowy0, Nowy1, Nowy2, Nowy3, Nowy4]

# Sortowanie listy
by_name = sorted(Wszyscy, key=lambda person: person.imie)
by_surname = sorted(Wszyscy, key=lambda person: person.nazwisko)
by_email = sorted(Wszyscy, key=lambda person: person.mail)
# Drukowanie posortowanej listy
#print(by_name)
#print(by_surname)
#print(by_email)


