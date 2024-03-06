import csv
import sqlite3

DATABASE = "SteamData_Dummy"
class Database(object):
    def __init__(self) -> None:
        self.conn = sqlite3.connect(DATABASE)
        self.cur = self.conn.cursor()

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
            self.connection.close()

    def insert_Games(self, values:tuple):
        """Order of the columns:
            gameID, gamename, releaseDate, languageEnglish,
            requiredAge, gameAchievements, positiveRatings,
            negativeRatings, averagePlaytime, medianPlaytime,
            gamePrice, gameOwners
        """
        try:
            conn.execute("""INSERT INTO Games
                           (gameID, gameName,
                            releaseDate, languageEnglish,
                            requiredAge, gameAchievements,
                            positiveratings, negativeRatings,
                            averagePlaytime, medianPlaytime, gamePrice)
                            Values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                            values)
        except sqlite3.Error:
            print("Something went wrong!")
    
    def insert_Developers(self):
        pass

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()

with open("steam.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[0].isdigit() == True:
            cur.execute("""INSERT INTO Games (gameID, gameName,
                                                  releaseDate, languageEnglish,
                                                  requiredAge, gameAchievements,
                                                  positiveratings, negativeRatings,
                                                  averagePlaytime, medianPlaytime, gamePrice)
                                           Values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                            (row[0], row[1], row[2], row[3], row[7], row[11],
                             row[12], row[13], row[14], row[15], row[17])
                            )
            
            
