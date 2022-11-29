"""
Arzoo Shahzad
CMSY-156
Lab8: Manage EmailAddress
"""
"""
Write an address book program that stores your contacts' names and
their email addresses.
The names and email addresses are originally stored in a file
called phonebook.in, in the format:
"""
# Your program should read from the file,
file = open("phonebook.in")
emailAddress = {}

# Your program should be storing the corresponding email addresses into a dictionary
for line in file:
    emailAddress[line.strip()] = file.readline().strip()

# print(emailAddress)
file.close()
"""
Then, the program should display a menu that lets the user enter
the numbers 1 through 5, each corresponding to a different menu
item:

#1. Look up email address
#2. Add new name and email address
#3. Change existing email address
#4. Delete name and email address
#5. Save and exit
"""
choice = input('Enter\n1) look up an email address\n2) add a new name and email address\n3) change an email address\n4) delete a name and email address\n5) save address book and exit:')
"""
        When the user enters 1, the program should prompt them for a name,
        and then print the corresponding email address. If there is no
        dictionary entry under that name, the program should print, "Sorry,
        no contact exists under that name."

    
        When the user enters 2, the program should prompt them for a name
        and an email address, then add a new key-value pair to the dictionary.

        When the user enters 3, the program should prompt them for a name
        and a new email address for that contact. It should change the
        value of the corresponding dictionary entry to match the new email
        address.

        When the user enters 4, the program should prompt them for a name
        and delete the corresponding dictionary entry.

        When the user enters 5, the program should write the names and
        email addresses in alphabetical order by first name to the file
        phonebook.out.
    """
while choice != '6':    
    if choice == '1':        
        name = input("Enter the name of a contact ")
        if name in emailAddress:
            print(emailAddress[name])
        else:
            print("Name not found")        
    elif choice == '2':        
        name = input("Enter a name of a new contact ")
        email = input("Enter an email of a new contact ")
        emailAddress[name] = email        
    elif choice == '3':        
        name = input("Enter a name of an existing contact ")
        email = input("Enter a new email address ")
        emailAddress[name] = email        
    elif choice == '4':        
        name = input("Enter a name of a contact to delete ")
        if name in emailAddress:
            del emailAddress[name]            
            print("Contact {%s} deleted" % name)
        else:
            print("Name not found in phonebook.in, please Try again!")
    elif choice == '5':
        print("Writing to phonebook.out")
        with open("phonebook.out", 'w') as f:
            for key, value in sorted(emailAddress.items()):
                f.write('{}\n{}\n'.format(key,value))
        break
    choice = input('Enter\n1) look up an email address\n2) add a new name and email address\n3) change an email address\n4) delete a name and email address\n5) save address book and exit:')
