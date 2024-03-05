import csv
from sqlalchemy import create_engine,  text

engine = create_engine("sqlite:///SteamData_Dummy.db",
                       future=True, echo=True)

conn = engine.connect()

result = conn.execute(text("SELECT gameName FROM Games"))

print(result.all())




# with open('steam.csv', mode="r") as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         if row[0].isdigit():
#             pass
            
            # cur.execute("""INSERT INTO Games (gameID, gameName, releaseDate,
            #             languageEnglish, requiredAge, gameAchievements,
            #             positiveRatings, negativeRatings, averagePlaytime,
            #             medianPlaytime, gamePrice)
            #             Values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            #             (row[0], row[1], row[2], row[3], row[7], row[11],
            #              row[12], row[13], row[14], row[15], row[17]))
            # connection.commit()

        

