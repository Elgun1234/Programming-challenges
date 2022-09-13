import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                csv_contents.append(row)
    return csv_contents


if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    team = "team"
    points = "points"
    goal_diff = "goal difference"
    

    dictionary = {}
    for row in file_contents:
        home = row[1]
        away = row[2]
        homegoals = row[3]
        awaygoals = row[4]
        winner = row[5]
        
        
        if home not in dictionary:
            dictionary[home] = [0,0]
        if away not in dictionary:
            dictionary[away] = [0,0]       

        if winner == "A":
            dictionary[away][0]+= 3
        elif winner == "H":
            dictionary[home][0]+=3
        else:
            dictionary[home][0]+=1
            dictionary[away][0]+=1
        
        
        gd = int(homegoals) - int(awaygoals)
        dictionary[home][1] += gd
        dictionary[away][1] -= gd
        gd = 0

    
    
    dic2 = {}
    for i in sorted(dictionary):
        dic2 = dict(sorted(dictionary.items(),key= lambda x:x[1],reverse=True))
    
    print(f"{team:17} {points:12} {goal_diff:20}\n")

    
    
    for key in dic2:
        
        point = dic2[key][0]
        goal_difference = dic2[key][1]
        print(f"{key:10} {point:10} {goal_difference:10}")

   
   

