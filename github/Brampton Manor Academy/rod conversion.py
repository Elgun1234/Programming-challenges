rods = float(input("rods "))
print("your input", rods)

def metres(rods):
    rods *= 5.0292
    
    return rods

    
def feet(f):
    f = x * 0.3048
    
    return(f)

def miles(m):
    m = x * 1609.34
    
    return(m)

def furlongs(rods):
    h = rods / 40
   
    return(h)

def walkspeed(m):
    ws = m / 60
    return ws

x = metres(rods)
print(rods)
f = feet(x)
print(x)
m = miles(x)
print(m)
h = furlongs(rods)
print(h)
ws = walkspeed(m)
print(ws)


