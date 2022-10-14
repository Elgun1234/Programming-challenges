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
    k=1
    for i in data:
        
        date = i[0]
        adj_close = float(i[5])
        volume = int(i[6])
        split_date = date.split("-")
        year_month = split_date[0] + "-" + split_date[1]
        future_date = data[k][0]
        
        if k <len(data)-1:
            k+=1
        
        split_future_date = future_date.split("-")
        future_year_month = split_future_date[0] + "-" + split_future_date[1]
        if year_month not in dictionary:            
            dictionary[year_month] = [0,0,0]
        dictionary[year_month][1] += volume
        dictionary[year_month][0] += volume * adj_close
        if k == len(data)-1:
            future_year_month + "1"
        if year_month != future_year_month:
            dictionary[year_month][2]=  dictionary[year_month][0] / dictionary[year_month][1]
    
         
                    
            
          
    ordered_dict = sorted(dictionary.items(), key=lambda x:x[1][2])
    for i in range(0,7):
        a = ordered_dict[i][0]
        b = ordered_dict[i][1][0]
        c = ordered_dict[i][1][1]
        d = ordered_dict[i][1][2]
        print(a,b,c,d)
     
        

data = reader()
apple(data)
