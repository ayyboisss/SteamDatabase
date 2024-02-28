import csv

with open('steam.csv', mode="r") as csv_file:
    reader = csv.reader(csv_file)
    try:
        for row in reader:
            print(row)
    except UnicodeDecodeError:
        pass
