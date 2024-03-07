import csv
from database_handler import Database

DATABASE = "Steamdata_Dummy.db"
Games = Database()
Games.set_Database(DATABASE)

def seperator_irator(text=str):
    """Seperate ';' from strings, returns a list"""
    result = text.split(sep=";")
    return result
    
temp_developers = []
temp_owners = []
temp_publishers = []
temp_categories = []


with open("steam.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # Handles Developers Table
        if row[4] != "developer":
            if row[4] not in temp_developers:
                Games.insert_Developers(row[4])
                temp_developers.append(row[4])
        # END OF DEVELOPERS 
        
        # Handles Publishers Table
        if row[5] != "publisher":
            if row[5] not in temp_publishers:
                Games.insert_Pubishers(row[5])
                temp_developers.append(row[5])
        # END OF PUBLISHERS TABLE
        
        if row[8] != "categories":
            for i in seperator_irator(row[8]):
                if i not in temp_categories:
                    print(i)
                    Games.insert_Categories(i)
                    temp_categories.append(i)
        
        # Handles Games Table
        if row[0].isdigit() == True:
            game_things = (
             row[0], row[1], row[2], row[3], row[7],
             row[11], row[12], row[13], row[6],
             row[14], row[15], row[17],
            ) # Goodluck figuring this out!
            Games.insert_Games(game_things) # ILOVEOBJECTS
        # END OF GAMES TABLE
print(Games.select_all("""SELECT categoryName FROM Categories"""))
print(temp_categories)

        
            
            
