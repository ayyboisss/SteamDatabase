import csv
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

Base = automap_base()
engine = create_engine("sqlite:///SteamData_Dummy.db",
                       future=True, echo=True)
# This took way too long to figure out
Base.prepare(autoload_with=engine)
Games = Base.classes.Games
session = Session(engine)

with open("steam.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[0].isdigit() == True:
            stmt = (
                insert(Games).values(
                    gameID = row[0],
                    gameName = row[1],
                    releaseDate = row[2],
                    languageEnglish = row[3],
                    requiredAge = row[7],
                    gameAchievements = row[11],
                    positiveRatings = row[12],
                    negativeRatings = row[13],
                    averagePlaytime = row[14],
                    medianPlaytme = row[15],
                    gamePrice = row[17],
                    )
                )
            
