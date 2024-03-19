import sqlite3

class Database(object):
    """Remember to commit()!!!"""

    def set_Database(self, DATABASE):
        self.DATABASE = DATABASE
        self.conn = sqlite3.connect(self.DATABASE)
        self.cur = self.conn.cursor()

    def exit(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def insert_Games(self, values:tuple):
        """Order of the columns:
            gameID, gamename, releaseDate, languageEnglish,
            requiredAge, gameAchievements, positiveRatings,
            negativeRatings, averagePlaytime, medianPlaytime,
            gamePrice, gameOwners
        """
        try:
            self.cur.execute("""
                                INSERT INTO Games
                                (gameID, gameName,
                                releaseDate, languageEnglish,
                                requiredAge, gameAchievements,
                                positiveratings, negativeRatings,
                                averagePlaytime, medianPlaytime,
                                gamePrice, gamePlatforms)
                                Values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                            values)
        except sqlite3.Error:
            print("Something went wrong!")
    
    def insert_Developers(self, developerName=str):
        self.cur.execute("""
                          INSERT INTO Developers (developerName)
                          Values (?)
                         """, (developerName,))
    
    def insert_Categories(self, categoryName):
        self.cur.execute("""
                          INSERT INTO Categories (categoryName)
                          Values (?)
                         """, (categoryName,))
    
    def insert_Tags(self, tagName):
        self.cur.execute("""
                          INSERT INTO Tags (tagName)
                          Values (?)
                         """, (tagName,))
    
    def insert_Pubishers(self, publisherName,):
        self.cur.execute("""
                          INSERT INTO Publishers (publisherName)
                          VALUES (?)
                         """, (publisherName,))
    
    def insert_Owners(self, ownerAmount):
        self.cur.execute("""
                          INSERT INTO Owners (ownerAmount)
                          VALUES (?)
                         """, (ownerAmount,))
    
    def insert_Genres(self, genreName):
        self.cur.execute("""
                          INSERT INTO Genres (genreName)
                          Values (?)
                         """, (genreName,))
    
    def update_GamesOwnerAmount(self, gameName, ownerAmount):
        gameID = self.selectGames_gameNameFor_gameID(gameName)
        self.cur.execute("""
                         UPDATE Games
                         SET ownerAmount = (?)
                         WHERE gameID = (?)
                         """, (ownerAmount, gameID,))

    def insert_gameDevelopers(self, gameName, developerName):
        gameID = self.selectGames_gameNameFor_gameID(gameName)
        developerID = self.selectDevelopers_developerNameFor_developerID(str(developerName))
        self.cur.execute("""
                         INSERT INTO gameDevelopers (gameID, developerID)
                         VALUES (?, ?)
                         """, (gameID, developerID,))

    def insert_gamePublishers(self, gameName, publisherName):
        gameID = self.selectGames_gameNameFor_gameID(gameName)
        publisherID = self.selectPublishers_publisherNameFor_publisherID(publisherName)
        self.cur.execute("""
                         INSERT INTO gamePublishers (gameID, publisherID)
                         VALUES (?, ?)
                         """, (gameID, publisherID,))
    
    def insert_gameTags(self, gameName, tagName):
        gameID = self.selectGames_gameNameFor_gameID(gameName)
        tagID = self.selectTags_tagNameFor_tagID(tagName)
        self.cur.execute("""
                         INSERT INTO gameTags (gameID, tagID)
                         VALUES(?, ?)
                         """, (gameID, tagID,))
    
    def insert_gameCategories(self, gameName, categoryName):
        gameID = self.selectGames_gameNameFor_gameID(gameName)
        categoryID = self.selectCategories_categoryNameFor_categoryID(categoryName)
        self.cur.execute("""
                         INSERT INTO gameCategories (gameID, categoryID)
                         VALUES (?, ?)
                         """, (gameID, categoryID,))
    
    def insert_gameGenres(self, gameName, genreName):
        gameID = self.selectGames_gameNameFor_gameID(gameName)
        genreID = self.selectGenres_genreNameFor_genreID(genreName)
        self.cur.execute("""
                         INSERT INTO gameGenres (gameID, genreID)
                         VALUES (?, ?)
                         """, (gameID, genreID,))

    def selectGames_gameNameFor_gameID(self, gameName):
        self.cur.execute("""SELECT gameID FROM Games WHERE gameName = (?)"""
                         , (gameName,))
        result = self.cur.fetchone()
        return result[0]

    def selectDevelopers_developerNameFor_developerID(self, developerName):
        self.cur.execute("""SELECT developerID FROM Developers WHERE developerName = (?)"""
                         , (developerName,))
        result = self.cur.fetchone()
        return result[0]

    def selectTags_tagNameFor_tagID(self, tagName):
        self.cur.execute("""SELECT tagID FROM Tags WHERE tagName = (?)"""
                         , (tagName,))
        result = self.cur.fetchone()
        return result[0]
    
    def selectCategories_categoryNameFor_categoryID(self, categoryName):
        self.cur.execute("""SELECT categoryID FROM Categories WHERE categoryName = (?)"""
                         , (categoryName,))
        result = self.cur.fetchone()
        return result[0]
    
    def selectPublishers_publisherNameFor_publisherID(self, publisherName):
        self.cur.execute("""SELECT publisherID FROM Publishers WHERE publisherName = (?)"""
                         , (publisherName,))
        result = self.cur.fetchone()
        return result[0]
    
    def selectGenres_genreNameFor_genreID(self, genreName):
        self.cur.execute("""SELECT genreID FROM Genres WHERE genreName = (?)"""
                         , (genreName,))
        result = self.cur.fetchone()
        return result[0]
    
    def selectGames_searchName(self, gameName):
        self.cur.execute("""
                         SELECT Games.gameName, Developers.developerName
                         FROM gameDevelopers
                         JOIN Games
                         ON Games.gameID = gameDevelopers.gameID
                         JOIN Developers ON
                         Developers.developerID = gameDevelopers.developerID
                         WHERE gameName LIKE (?)
                         """, (f"%{gameName}%", ))
        result = self.cur.fetchall()
        return result

    def select_all(self, QUERY):
        """A function for debugging, REMOVE if finished"""
        self.cur.execute(QUERY)
        result = self.cur.fetchall()
        return result[0]
    