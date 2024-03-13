import csv
from database_handler import Database

DATABASE = "Steamdata_Dummy2.db"
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
            if row[4] not in temp_developers:
                for i in seperator_irator(row[4]):
                    Games.insert_Developers(i)
                    temp_developers.append(i)
                    game_tempDevelopers.append(i)
        # END OF DEVELOPERS 
        
        # Handles Publishers Table
        if row[5] != "publisher":
            if row[5] not in temp_publishers:
                for i in seperator_irator(row[5]):
                    Games.insert_Pubishers(i)
                    temp_publishers.append(i)
                    game_tempPublishers.append(i)
        # END OF PUBLISHERS TABLE
        
        # Handles Categories Table
        if row[8] != "categories":
            for i in seperator_irator(row[8]):
                if i not in temp_categories:
                    Games.insert_Categories(i)
                    temp_categories.append(i)
                    game_tempCategories.append(i)
        # END OF Categories Table
        
        # Handles Genres Table
        if row[9] != "genres":
            for i in seperator_irator(row[9]):
                if i not in temp_genres:
                    Games.insert_Genres(i)
                    temp_genres.append(i)
                    game_tempGenres.append(i)
        # END OF Genres Table

        # Handles Tags Table
        if row[10] != "steamspy_tags":
            for i in seperator_irator(row[10]):
                if i not in temp_tags:
                    Games.insert_Tags(i)
                    temp_tags.append(i)
                    game_tempTags.append(i)
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
            print(row[1] + " Game Name!!! ")
            # It hurts to look at
            for x in game_tempCategories:
                i = Games.selectCategories_categoryNameFor_categoryID(x)
                Games.insert_gameCategories(row[1], str(i))
            for x in game_tempDevelopers:
                i = Games.selectDevelopers_developerNameFor_developerID(x)
                Games.insert_gameDevelopers(row[1], str(i))
            for x in game_tempGenres:
                i = Games.selectGenres_genreNameFor_genreID(x)
                Games.insert_gameGenres(row[1], str(i))
            for x in game_tempPublishers:
                i = Games.selectPublishers_publisherNameFor_publisherID(x)
                Games.insert_gamePublishers(row[1], str(i))
            for x in game_tempTags:
                i = Games.selectTags_tagNameFor_tagID(x)
                Games.insert_gameTags(row[1], str(i))
        # END OF GAMES TABLE
        




Games.commit()
Games.exit()

            
            
