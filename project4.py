1
def main():
    contacts = {}


    while True:
        choice = get_menu_choice()
        if choice == 6:
            break
        elif choice == 1:
            view(contacts)

        elif choice == 2:
            add(contacts)


        elif choice == 3:
            search(contacts)

        elif choice == 4:
            update(contacts)

        elif choice == 5:
            delete(contacts)

        option = int(input("1. Return to menu\n2. Quit \n"))
        if option == 2:
            break



def get_menu_choice():
    print('Contacts\n========\n1. View Contacts\n2. Add New Contact\n3. Search\n4. Update Contact\n5. Delete Contact\n6. Quit')
    choice = int(input("Enter a choice number: "))
    if choice in range(1,7):
        return choice
    else:
        print("Please enter in a valid choice ")

def view(c):
    if c == {}:
        print('You have no contacts yet')
    else:
        for k,v in c.items():
            print(f'{k}: {v}')

def add(con):
    name = input('Enter in a name: ')
    number = input('Enter in a number: ')
    con[name] = number

def search(ct):
    looking_for = input('Enter in a name: ')
    if looking_for in ct:
        print(ct.get(looking_for))
    else:
        print("not found")


def update(cts):
    n = input("Enter in a name: ")
    if n in cts:
        new_num = input("Enter in a new number: ")
        cts[n] = new_num
    else:
        print("not found")

def delete(c_):
    name_to_delete = input("Enter in a name to delete: ")
    if name_to_delete in c_:
        del c_[name_to_delete]
        print("the name is deleted")





main()