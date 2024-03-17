import csv
from database_handler import Database

DATABASE = "Steamdata.db"
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
temp_genres = []
temp_tags = []

with open("steam.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        game_tempTags = []
        game_tempDevelopers = []
        game_tempGenres = []
        game_tempPublishers = []
        game_tempCategories = []
        
        # Handles Developers Table
        if row[4] != "developer":
            for i in range(0, len(seperator_irator(row[4]))):
                game_tempDevelopers.append(seperator_irator(row[4])[i])
                if seperator_irator(row[4])[i] not in temp_developers:
                    developer = seperator_irator(row[4])[i]
                    temp_developers.append(developer)
                    Games.insert_Developers(developer)
        # END OF DEVELOPERS 
        
        # Handles Publishers Table
        if row[5] != "publisher":
            for i in range(0, len(seperator_irator(row[5]))):
                game_tempPublishers.append(seperator_irator(row[5])[i])
                if seperator_irator(row[5])[i] not in temp_publishers:
                    publisher = seperator_irator(row[5])[i]
                    temp_publishers.append(publisher)
                    Games.insert_Pubishers(publisher)
        # END OF PUBLISHERS TABLE
        
        # Handles Categories Table
        if row[8] != "categories":
            for i in seperator_irator(row[8]):
                game_tempCategories.append(i)
                if i not in temp_categories:
                    Games.insert_Categories(i)
                    temp_categories.append(i)

        # END OF Categories Table
        
        # Handles Genres Table
        if row[9] != "genres":
            for i in seperator_irator(row[9]):
                game_tempGenres.append(i)
                if i not in temp_genres:
                    Games.insert_Genres(i)
                    temp_genres.append(i)

        # END OF Genres Table

        # Handles Tags Table
        if row[10] != "steamspy_tags":
            for i in seperator_irator(row[10]):
                game_tempTags.append(i)
                if i not in temp_tags:
                    Games.insert_Tags(i)
                    temp_tags.append(i)

        # END OF Tags Table
        
        # Handles Owners Table
        if row[16] != "owners":
            if row[16] not in temp_owners:
                Games.insert_Owners(row[16])
                temp_owners.append(row[16])
        # END OF Owners Table

        # Handles Games Table
        if row[0].isdigit():
            game_things = (
             row[0], row[1], row[2], row[3], row[7],
             row[11], row[12], row[13], row[6],
             row[14], row[15], row[17],
            ) # Goodluck figuring this out!
            Games.insert_Games(game_things) # ILOVEOBJECTS
            Games.update_GamesOwnerAmount(row[1], row[16])
            # It hurts to look at.
            # There was no way to put this in one 'for' function
            # as it would either index out of range (and potentially
            # put nothing) or would not be enough. It doesn't slow down
            # the program as much anyways.
            for x in game_tempCategories:
                Games.insert_gameCategories(row[1], x)
            for x in game_tempDevelopers:
                Games.insert_gameDevelopers(row[1], x)
            for x in game_tempGenres:
                Games.insert_gameGenres(row[1], x)
            for x in game_tempPublishers:
                Games.insert_gamePublishers(row[1], x)
            for x in game_tempTags:
                Games.insert_gameTags(row[1], x)
        # END OF GAMES TABLE
Games.commit()
Games.exit()

            
            
