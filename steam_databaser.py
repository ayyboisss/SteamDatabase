import os
from database_handler import Database
from time import sleep


DATABASE = "SteamData.db"
tables = Database()
tables.set_Database(DATABASE)


def clear():
    os.system("cls")


def user_input():
    try:
        inp = int(input())
    except ValueError:
        inp = None
    else:
        return inp
    

def show_result(result=tuple, columns=tuple):
    limit_flag = False
    x = 0
    while True:
        print(" ".join(columns))
        if len(result) > 5:
            for i in range((0 + x), (4 + x)):
                try:
                    print("".join(result[i]))
                except IndexError:
                    limit_flag = True
                    print(" ")
            next_page = input("Enter N / B to go to the next / last page, otherwise \
                                  enter nothing to go back to the main menu \n")
            if next_page.capitalize() == "N":
                if limit_flag:
                    pass
                else:
                    x += 5
            elif next_page.capitalize() == "B":
                if x == 0:
                    pass # While loop will take care of these whippersnappers
                else:
                    x -= 5
            else:
                menu()
                
                
        elif len(result) > 0:
            for i in len(result):
                print("".join(i))

    


def menu_title(title):
    clear()
    print("--"*10)
    print(f"{title}")

def menu():
    menu_title("Steam Data Menu:")
    print("1. Search \n2. Insert \n3. Delete \n4. Update")
    while True:
        menu_inp = user_input()
        if menu_inp == 1:
            search_menu()
        else:
            print("Invalid input")


def search_menu():
    menu_title("Table to search:")
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
    menu_title("Search by:")
    print("1. Name \n2. Game ID \n3. Developer")
    while True:
        game_inp = user_input()
        if game_inp == 1:
            select_games_name()
            
def select_games_name():
    menu_title("Searching...")
    search_name = input("Name of the game: ")
    result = tables.selectGames_searchName(search_name)
    show_result(result, ("Name", "Developer"))


def search_developers():
    pass


def search_publishers():
    pass


# This is a dumb idea, do NOT do this
menu()
