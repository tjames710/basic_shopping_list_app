# have a HELP command
# have a SHOW command




# make a list to hold onto our items
shopping_list = []

def show_help():
    # print out instructions on how to use the app
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
Enter 'REMOVE' to remove an item by name.
""")

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

def remove_item():
    item = input("What item would you like removed > ")
    shopping_list.remove(item)
    print("item {} has been removed. List now has {} items.".format(item, len(shopping_list)))
    

        

def show_list():
    print("Here's your list: ")
    for item in shopping_list:
        print(item)



def main():
    show_help()

    while True:
        # ask for new items
        new_item = input("> ")

        # be able to quit the app
        if new_item == "DONE":
            break
        elif new_item == "HELP":
            show_help()
            continue
        elif new_item == "SHOW":
            show_list()
            continue
        elif new_item == "REMOVE":
            remove_item()
            continue
            


        add_to_list(new_item)


    # print out the list
    show_list()

main()