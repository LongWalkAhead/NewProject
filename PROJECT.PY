dictionary = {'person 1':{"name": "Carley", "number": "111-222-333", "email": "Carley@example.com"},"person 2":{"name": "David", "number": "333-444-555", "email": "David@example.com"}, "person 3":{"name": "Sophia", "number": "666-777-888", "email": "sophia@example.com"}}

menu = input("Welcome to the contact management system!\n 1. Add a new Contact\n 2.edit an existing contact\n 3. delete a contact \n 4. search for a contact\n 5. display all contact\n 6. export contacts to text file\n 8. quit ")


def adding_new_contact():
    try:
        dictionary.setdefault("person 4",{"name": "Joe", "number": "166-266-366", "email": "Joe@example.com"})
    except: SyntaxError
    else: 
        print(dictionary)
        
    

if menu == "1":
    adding_new_contact()
    print(f"contact added sucessfully!")

def editing_contact():
    dictionary.update('person 1',{"name": "Carley", "number": "111-234-333", "email": "Carley@example.com"})
    #print("contact updated successfully")

if menu == "2":
    editing_contact()
    print("contact edited succesfully!")

def deleting_contact(person):
    try:
        del dictionary[person]
        print(dictionary)
    except: TypeError

if menu == "3":
    deleting_contact("person 3")
    print("contact deleted successfully!")

def searching_for_contact():
    finding_david = dictionary["person 2"]
    print(finding_david)

if menu == "4":
    searching_for_contact()
    
def displaying_contacts():
    for person, info in dictionary.items():
        for keys, values in info.items():
            print(f"{keys}: {values}")

if menu == "5":
    displaying_contacts()


def exporting_file():
   try:
    with open("myproject.txt", 'w') as file:
        for person, info in dictionary.items():
            for keys, values in info.items():
                file.write(f"{keys}: {values}\n")
   except:Exception
   print("error, something may be wrong")
   
   if menu == "6": 
    exporting_file()