import operator
from pdb import Restart
import sys
from faker import Faker

fake = Faker('pl_PL')
names = []

# GŁOWNA KLASA
class AdressBook():
    def __init__(self, firstname, lastname, job, email, company):
        self.firstname = firstname
        self.lastname = lastname
        self.job = job
        self.email = email
        self.company = company

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.job} {self.email} {self.company}'

    def __repr__(self):
        return f'AdressBook(firstname={self.firstname}, lastname={self.lastname}, job={self.job}, email={self.email} company={self.company})'
        
    def contact(self):
        return f'Kontaktuje się z {self.firstname} {self.lastname} pracującym na stanowisku {self.job}. Jego e-mail to: {self.email}'

# SUMOWANIE ZNAKOW IMIĘ + NAZWISKO
    @property
    def count(self):
        return sum([len(self.first_name), len(self.last_name), 1])

# KLASY DZIEDZICZONE

class BaseContact(AdressBook):
    def __init__(self, tel_private, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone = tel_private

    def contact(self):
        return f'Wybieram numer prywatny: {self.phone} i dzwonię do {self.firstname} {self.lastname}.'

    @property
    def label_length(self):
        return sum([len(self.first_name), len(self.last_name)])

# --------------------------------------

class BusinessContact(AdressBook):
    def __init__(self, tel_work, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone= tel_work

    def contact(self):
        return f'Wybieram numer słubowy: {self.phone} i dzwonię do {self.firstname} {self.lastname}.'

    @property
    def label_length(self):
        return sum([len(self.first_name), len(self.last_name)])

# GENEROWANIE WIZYTOWEK BASE

def base(count):
    for contact in range(count):
        contact = BaseContact(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            company=fake.company(),
            job=fake.job(),
            email=fake.email(),
            tel_private=fake.phone_number()
            )
        names.append(contact)
        print() 
        print((contact))
        print(contact.contact())
        return names
        
# GENEROWANIE WIZYTOWEK BUSINESS

def business(count):
    for contact in range(count):
        contact = BusinessContact(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            company=fake.company(),
            job=fake.job(),
            email=fake.email(),
            tel_work=fake.phone_number()
            )
        names.append(contact)
        print() 
        print((contact))
        print(contact.contact())
        return names

# DEFINICJA TWORZENIA KONTAKTOW

def create_contacts():
    my_type = input("\n Jakiego typu wizytówki chcesz utworzyć?\n Wpisz: 'basic' lub 'extended'.\n Aby zakończyć dzialanie programu wpisz 'exit'\n\n")
    if my_type == "basic":
        count = int(input("Ile wizytówek chcesz wygnerować? (Podaj liczbe:) "))
        base(count)
            
    elif my_type == "extended":
        count = int(input("Ile wizytówek chcesz wygnerować? (Podaj liczbe:) "))
        business(count)

    elif my_type == "exit":
        exit()
    
    else:
        error = f"Nieprawidłowy wybór. Spróbuj ponownie lub wpisz 'exit', aby zakończyć program."
        print(error)

# SORTOWANIA 

def by_name(names):
    print("Sortowanie po imieniu:")
    _by_name = sorted(names, key=operator.attrgetter('firstname'))
    names = _by_name
    print(names)
    return names

def by_lastname(names):
    print("Sortowanie po nazwisku:")
    _by_lastnamename = sorted(names, key=operator.attrgetter('lastname'))
    names = _by_lastnamename
    print(names)
    return names

def by_email(names):
    print("Sortowanie po e-mail:")
    _by_email = sorted(names, key=operator.attrgetter('email'))
    names = _by_email
    print(names)
    return names


# DZIAŁANIE PROGRAMU

if __name__ == "__main__":

    print("Wybierz proszę co chcesz zrobić?\n\n 1 - nowa wizytówka\n 2 - sortowanie kontaktów wg. imienia\n 3 - sortowanie kontaktów wg. nazwiska\n 4 - sortowanie kotnatków wg. e-mail\n\n 'exit' zakończenie działania programu\n")

    choice = input("Twój wybór: ")
    
    names = names
    
    while True: 
        if choice == "1":
            create_contacts()
            continue
            
        elif choice == "2":
            by_name(names)
            continue
        
        elif choice == "3":
            by_lastname(names)
            continue
        
        elif choice == "4":
            by_email(names)
            continue
        
        elif choice == "exit":
            print("                       ")
            print("Wpadnij jeszcze kiedyś!")
            print("                       ")
            exit()

        else:
            error = f"Error!"
            print(error)
            exit()