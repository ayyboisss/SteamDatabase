import csv
from database_handler import Database

DATABASE = "Steamdata_Dummy.db"
Games = Database()
Games.set_Database(DATABASE)

with open("steam.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[0].isdigit() == True:
            game_things = (
             row[0], row[1], row[2], row[3], row[7],
             row[11], row[12], row[13],
             row[14], row[15], row[17]
            )
            Games.insert_Games(game_things) # ILOVEOBJECTS
print(Games.select_all("""SELECT gameName FROM Games"""))

        
            
            
