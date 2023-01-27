# Python implementation of menu driven
# Phone Book Directory
from time import sleep

contact = {}
inputList = ['1' , 'cool 123456789',
             'y', '2', 'cool', 'n']
indi = -1
# function to provide sample inputs
# remove this function to run on custom inputs
#def input():
#    global indi
#    indi += 1
#    print(' inputList: {}'.format(inputList[indi]))
#    return inputList[indi]

def delete_contact():
    global contact
    print(' Enter the contact name to be deleted.')
    name = str(input(' ')).strip()
    if name in contact:
        del(contact[name])
        print(' Contact deleted!\n')
    else:
        print(' Contact not found...')

    print(' Do you want to perfom more'\
          ' operations? (y / n) ')
    choice = input().strip()
    if choice in 'YyYesyes':
        main()
    else:
        print('\n Thank you. Have a nice day!\n')

def update_contact():
    global contact
    print(' Enter the contact name to be updated.')
    name = str(input(' ')).strip()
    if name in contact:
        print('  Now enter the new contact number = ')
        phone = int(input())
        contact[name] = phone
        print(' Contact successfully updated')
    else:
        print(' Contact has not been found.')

    print(' Do you want to perfom more'\
          ' operations? (y / n) ')
    choice = input().strip()
    if choice in 'YyYesyes':
        main()
    else:
        print('\n Thank you. Have a nice day!\n')

def search_contact():
    global contact
    print(' Enter the name to be searched - ')
    name = input().strip()
  
    if name in contact:
        print('Contact Found !')
        print(' Name: ', name, ' Phone: ', contact[name])
    else:
        print('  Contact not found !\n')
  
  
    print(' Do you want to perform more'\
        ' operations? (y / n) ' )
  
    choice = input().strip()
    if choice == 'y':
        main()
    else:
        print('\n Thank you. Have a nice day!\n')
    
def store_contact():
    print("\n\nEnter the name"\
        " and phone number"+\
        " separated by space - ")

    name, phone = map(str, input().strip().split(' '))
    global contact
    if name in contact:
        print(' Contact already exists!\n')
    else:
        contact[name] = phone
        print(' Contact successfully stored!')
        
    print(' Do you want to perform more'\
        ' operations? (y / n) ' )
    choice = input().strip()
    if choice == 'y':
        main()
    else:
        print('\n Thank you. Have a nice day!\n')

def show_contacts():
    global contact
    for k, v in contact.items():
        print(' | Name : ', k, '| Phone: ', v, '|')
        sleep(0.3)
    print(' Do you want to perform more'\
        ' operations? (y / n) ' )
    choice = input().strip()
    if choice == 'y':
        main()
    else:
        print('\n Thank you. Have a nice day!\n')

def main():
    print("\nPlease choose any choice"\
        " from below -\n\n\n")
    print("Store Contact number .... (1)")
    print("Search Contact number ... (2)")
    print("Update Contact number ... (3)")
    print("Delete Contact number ... (4)")
    print("Show stored Contacts .... (5)")

    choice = int(input())
    actions = {
        1: store_contact,
        2: search_contact,
        3: update_contact,
        4: delete_contact,
        5: show_contacts
        }
    if choice in actions:
        actions[choice]()
    else:
        print(' Invalid operation.')
        main()


if __name__ == "__main__":
    try:
        print("----------------------"+\
              "Welcome to GeeksforGeeks Phonebook"+\
              "----------------------")
        main()
        
    except KeyboardInterrupt:
        print('\n Program has been stopped. Goodbye')
