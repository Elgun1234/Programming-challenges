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
    return data


def apple(data):
    dictionary = {}
    vol = 0
    for i in data:
        date = i[0]
        adj_close = float(i[5])
        volume = int(i[6])
        split_date = date.split("-")
        year_month = split_date[0] + "-" + split_date[1]
        if year_month not in dictionary:            
            dictionary[year_month] = [0,0,0]
            dictionary[year_month][0] += adj_close * volume
            dictionary[year_month][1] += volume
            dictionary[year_month][2] += dictionary[year_month][0] / dictionary[year_month][1] 
            
        else:            
            dictionary[year_month][0] += adj_close * volume
            dictionary[year_month][1] += volume
            dictionary[year_month][2] += dictionary[year_month][0] / dictionary[year_month][1] 
    print(dictionary)    

   
        
        

data = reader()
apple(data)
