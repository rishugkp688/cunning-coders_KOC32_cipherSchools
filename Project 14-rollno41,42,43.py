contacts={
"ARYANSH": 7898798791,
"KARRISYAM": 1234567890,
"VANTUBUSASI": 1233443166
}

def single_search():
    name=input("Enter name to search").upper()
    if name in contacts:
        print(f"\n{name}: {contacts[name]}")
    else:
        b=input("\nNo contact found")

def multiple_search():
    result={}
    s1=[]
    s=0
    name1=input("Enter the names of the contacts").split(",")
    for i in name1:
        i=i.upper()
        if i in contacts:
            result[i]=contacts[i]
        else:
            s1.append(i)
            s+=1
    if s>0:
        c=input(f"\nCouldn't find contacts {s1}")
    else:
        print()
        print(result)
def new_contact(contact_name):
    print()
    contact_number=int(input("Enter their contact number:"))
    contacts[contact_name]=contact_number

while True:

    choice=int(input("Would you like to: \n\n1. Search for a single contact\n2. List all the contacts\n3. Search for multiple contacts\n4. Add contact\n5.Exit\n"))
    if choice==1:
        single_search()
    elif choice==2:
        print()
        print(contacts)
    elif choice==3:
        multiple_search()
    elif choice==4:
        contact_name=input("Enter name: ")
        new_contact(contact_name)
    elif choice==5:
        break
    else:
        print("Please select a valid option")
