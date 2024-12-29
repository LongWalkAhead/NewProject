dictionary = {"Carley@example.com":{"name": "Carley", "number": "111-222-333", "email": "Carley@example.com"}}

def adding_new_contact(name, number, email):
    try:
        dictionary[email]= {"name": name, "number": number, "email": email}
    except:
        print("error for contact")
    else: 
        print(dictionary)
        

def editing_contact(email):
    if email in dictionary:
        print("1. name\n 2.numbers\n 3.email\n")
        option = input("what option would you like to choose? ")
        if option == "1":
            new_name = input("what is the new name? ")
            dictionary[email]["name"]=new_name
        elif option == "2":
            new_number = input("what is the new number? ")
            dictionary[email]["number"]=new_number
        elif option == "3":
            new_email = input("what is your new email?")
            dictionary[email]["email"]= new_email
    print("contact updated successfully")



def deleting_contact(email):
        if email in dictionary:
            del dictionary [email]
            print("contact deleted successfully!")
        else:
            print("contact does not exist.")


def searching_for_contact(email):
    if email in dictionary:
        contact_data = dictionary[email]
        for keys, values in contact_data.items():
            print(f"{keys}: {values}")
    else:
        print("this contact doesnt exist.")


def displaying_contacts():
    for person, info in dictionary.items():
        for keys, values in info.items():
            print(f"{keys}: {values}")



def exporting_file():
    try:
        with open("myproject.txt", 'w') as file:
            for person, info in dictionary.items():
                for keys, values in info.items():
                    file.write(f"{keys}: {values}\n")
    except:
        print("error, something may be wrong")
   
  

while True:
    menu = input("Welcome to the contact management system!\n 1. Add a new Contact\n 2.edit an existing contact\n 3. delete a contact \n 4. search for a contact\n 5. display all contact\n 6. export contacts to text file\n 8. quit ")
    if menu == "1":
        name = input("enter contact name: ")
        number = input("enter contact number: ")
        email = input("enter contact email: ")
        adding_new_contact(name, number, email)
    elif menu == "2":
        email = input("what email would you like to edit?")
        editing_contact(email)
    elif menu == "3":
        email = input("what email would you like to delete?")
        deleting_contact(email)
    elif menu == "4":
        email = input("what email would you like to search for?")
        searching_for_contact(email)
    elif menu == "5":
        displaying_contacts()
    elif menu == "6":
        exporting_file()
    else:
        print("this program will close, thank you!")
        break