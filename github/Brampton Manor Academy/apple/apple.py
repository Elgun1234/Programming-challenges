import csv
from pathlib import Path
def reader():
    data = []
    apple_csv = Path("AAPL.csv")
    with open(apple_csv) as apple_file:
        apple_data = csv.reader(apple_file, delimiter=",")
        next(apple_data)
        for i in apple_data:
            data.append(i)
def apple():
    dictionary = {}
    for i in data:
        date = data[0]
         date.
        


