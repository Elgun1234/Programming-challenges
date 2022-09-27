import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"

def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def finder():
    k = 0
    i = 0
    pos = "Postion"
    song = "Song"
    art = "Artist"
    print(f"{pos:45} {song:45} {art}\n")
    while k <10:        
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)
        newstring = html[open_tr:close_tr]
        lookingfor = '"position">'
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find('</', pos_start)
        rank = newstring[pos_start+len(lookingfor):pos_end]
        i = close_tr 
        lookingfor2 = '/">' 
        name_open = newstring.find('/">')
        name_close = newstring.find('</a>')
        name  = newstring[name_open+len(lookingfor2):name_close]
        artist_open = newstring.find('/">',name_close)
        artist_close = newstring.find('</a>',artist_open)
        artist = newstring[artist_open+len(lookingfor2):artist_close]
        print(f"{rank:>3} {name:>50} {artist:>60}")
        k += 1
    

if __name__ == "__main__":
    html = scrape(url)
    finder()

    
