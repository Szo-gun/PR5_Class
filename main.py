from cgi import test
from re import I
from tracemalloc import start
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
        print(f"Kontaktuję się z: {person.imie} {person.nazwisko}")


#Rozszerzenie klasy Event na klasę Base i Business

class BaseContact(event):
   def __init__(self, telefon_prywatny, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.telefon_prywatny = telefon_prywatny
       
   def contact_PR(self):
       print(f"Kontaktuję się z: {person.imie} {person.nazwisko} i dzwonię pod: {person.telefon_prywatny}")

def dane_PR(name):
    return(name.imie, name.nazwisko, name.mail, name.telefon_prywatny)

#JAK ZROBIĆ OPCJONALNY?!?!?!?!
class BusinessContact(event):
    def __init__ (self, telefon_biznes, *args, **kwargs):
    #def __init__ (self, stanowisko, firma, telefon_biznes, *args, **kwargs):
       super().__init__(*args, **kwargs)
       #self.stanowisko = stanowisko
       #self.firma = firma
       self.telefon_biznes = telefon_biznes
    
    def contact_BU(self):
        print(f"Kontaktuję się z {person.imie} {person.nazwisko} i dzwonię pod: {person.telefon_biznes}")

def dane_BU(name):
    return(name.imie, name.nazwisko, name.mail, name.telefon_biznes)

decision = input("Podaj czy chcesz wyświetlić kontakty prywatne [P], czy biznesowe [B]: ")
wybor = decision.upper()
if wybor == 'P':
# Pętla generująca 5 losowych wizytówek prywatnych
    for i in range(0,5):
        person = BaseContact(imie=fake.first_name(), nazwisko=fake.last_name(), mail=fake.email(),telefon_prywatny = fake.phone_number())
        dane_PR(person) 
        globals()["Nowy%s" % i] = person
        BaseContact.contact_PR(person)
        event.imie_len(person.imie)
        event.nazwisko_len(person.imie)
elif wybor == 'B':
# Pętla generująca 5 losowych wizytówek biznesowych
    for i in range(0,5):
        person = BusinessContact(imie=fake.first_name(), nazwisko=fake.last_name(), mail=fake.email(),telefon_biznes = fake.phone_number())
        dane_BU(person) 
        globals()["Nowy%s" % i] = person
        BusinessContact.contact_BU(person)
        event.imie_len(person.imie)
        event.nazwisko_len(person.imie)
else:
    print("Nie ma takiej wizytówki")

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


