import os
from database_handler import Database
from time import sleep

def clear():
    os.system("cls")

DATABASE = "SteamData.db"
tables = Database()
tables.set_Database(DATABASE)

def user_input():
    try:
        inp = int(input())
    except ValueError:
        inp = None
    else:
        return inp

def menu():
    clear()
    print("--"*10)
    print("SteamData Menu:")
    print("1. Search \n2. Insert \n3. Delete \n4. Update")
    while True:
        menu_inp = user_input()
        if menu_inp == 1:
            search_menu()
        else:
            print("Invalid input")
        


def search_menu():
    clear()
    print("--"*10)
    print("Table to search:")
    print("1. Games \n2. Developers \n3. Publishers")
    while True:
        search_inp = user_input()
        if search_inp == 1:
            search_games()
        elif search_inp == 2:
            search_developers()
        elif search_inp == 3:
            search_publishers()
        else:
            print("Invalid input")
    
def search_games():
    clear()
    print("--"*10)
    print("Select by:")
    print("1. Name \n2. Game ID \n3. Developer")
    pass

def search_developers():
    pass

def search_publishers():
    pass
    


# This is a dumb idea, do NOT do this
menu()
    
    

