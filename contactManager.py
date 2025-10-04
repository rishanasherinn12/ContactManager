class Contact:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
    def __str__(self):
        return f"Name:{self.name},Email:{self.email},Phone:{self.phone}"
class ContactManager:
    def __init__(self):
        self.contacts=[]
    def addContact(self,name,email,phone):
        cont=Contact(name,email,phone)
        self.contacts.append(cont)
        print("contact added succesfully!")
    def viewContact(self):
        if not self.contacts:
            print("contact not found")
        for cont in self.contacts:
            print(cont)
    def searchContact(self,name):
        for cont in self.contacts:
            if cont.name.lower()==name.lower():
                print(cont,"-->contact found")
                break
        else:
            print("Contact not found")

manager=ContactManager()
while True:
    print("1.Add contact\n2.view contact\n3.search contact\n4.exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=(input("Enter your name:"))
        email=(input("Enter your email:"))
        phone=int(input("Enter your phone no:"))
        manager.addContact(name,email,phone)
    elif choice==2:
        manager.viewContact()
    elif choice==3:
        searchName=(input("Enter the name to be search:"))
        manager.searchContact(searchName)
    elif choice==4:
        print("Exiting..")
        break
    else:
        print("invalid choice")

