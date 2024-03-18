import os
from database_handler import Database
from time import sleep

def clear():
    os.system("cls")

DATABASE = "SteamData.db"
tables = Database()
tables.set_Database(DATABASE)

def user_input():
    pass

def menu():
    print("--"*10)
    print("SteamData Menu:")
    print("1. Search \n2. Insert \n3. Delete \n4. Update" )

def search_menu():
    print("--"*10)
    print("Table to search:")
    print("1. Games \n2. Developers \n3. Publishers")

while True:
    menu()
    try:
        user_input = int(input())
    except ValueError:
        print("That isn't a number innit?")
        sleep(1)
    else:
        if user_input == 1:
            # Search Menu, This will branch out alot.
            clear()
            search_menu()

    

