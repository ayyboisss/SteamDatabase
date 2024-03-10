import sqlite3

class Database(object):
    """Remember to commit()!!!"""

    def set_Database(self, DATABASE):
        self.DATABASE = DATABASE
        self.conn = sqlite3.connect(self.DATABASE)
        self.cur = self.conn.cursor()

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.conn.rollback()
        else:
            self.conn.commit()
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
        self.cur.execute("""SELECT gameID FROM Games
                         WHERE gameName = (?)""", (gameName,))
        gameID = self.cur.fetchone()
        self.cur.execute("""UPDATE Games SET ownerAmount = (?)
                            WHERE gameID = (?)""", (ownerAmount, gameID,))


    
    def select_all(self, QUERY):
        """A function for debugging, REMOVE if finished"""
        self.cur.execute(QUERY)
        result = self.cur.fetchall()
        return result