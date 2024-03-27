import os
from database_handler import Database
from math import ceil
from msvcrt import getch
from time import sleep


DATABASE = "SteamData.db"
tables = Database()
tables.set_Database(DATABASE)


def clear():
    "Use this instead of typing 'os.' to clear the console"
    os.system("cls")


def user_input():
    "Returns None if the input is not a number."
    inp = getch().decode("ASCII")
    if inp == """\x1b""":
        return True
    try:
        inp = int(inp)
    except ValueError:
        inp = None
    else:
        return inp


def show_result(result=tuple, columns=tuple):
    "This will give a paged (if possible) screen to deal with the SQL queries"
    page_turn = 4
    limit_flag = False
    x = 0
    current_page = 1
    page_limit = ceil(len(result) / page_turn)
    while True:
        if len(result) > page_turn:
            clear()
            print(f"Result: {columns[0]} with {columns[1]} ({current_page} / {page_limit}) \n")
            for i in range((0 + x), (page_turn + x)):
                try:
                    print(f"{columns[0]}: {result[i][0]}")
                    print(f"{columns[1]}: {result[i][1]} \n")
                except IndexError:
                    limit_flag = True
                    print(" ")
            print("Enter N / B to go to the next / last page, " +
                  "otherwise enter nothing to go back to the main menu \n")
            next_page = getch().decode("ASCII")
            print(next_page)
            
            if next_page.capitalize() == "N":
                if limit_flag:
                    pass
                else:
                    current_page += 1
                    x += page_turn
            elif next_page.capitalize() == "B":
                limit_flag = False
                if x == 0:
                    pass # While loop will take care of these whippersnappers
                else:
                    current_page -= 1
                    x -= page_turn
            else:
                menu()
                
                
        elif len(result) > 0:
            for i in result:
                print(" ".join(i))
            
            end_search = input("Press Enter to go back to the menu, " +
                               "or press S to search again")
            if end_search.capitalize() == "S":
                search_menu()
            else:
                menu()


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
        elif menu_inp:
            break
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
