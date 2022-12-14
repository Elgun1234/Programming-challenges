import csv 
from pathlib import Path 

csv_file = Path("south.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            
            for row in reader:
                csv_contents.append(row)
            
    return csv_contents

def function(csv_contents):
    file = open("south.html", "r+")
    file_text = file.read()
    
    k=0
    b = 0
    for row in csv_contents:
        picture = row[0]
        
       
        url_open = file_text.find('url("',k+1)
        link = file_text[url_open+4:url_open+11]
        o = file_text.replace( link, picture)
        k = url_open
        file_text = o

    for row in csv_contents:
        initial = row[1]
        initials_open = file_text.find('ing">',b+1)
        initial_replace = file_text[initials_open+5:initials_open+14]
        h = file_text.replace(initial_replace,initial)
        file_text = h
        
        b = initials_open
    file.close()
    file = open("south.html", "w")
    file.seek(0)
    file.write(file_text)
    
    file.close()

if __name__ == "__main__":
    c = check_file_exists(csv_file)
    z = read_csv(csv_file)   
    function(z)
