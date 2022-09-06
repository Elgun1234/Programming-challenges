rods = float(input("rods "))
print("your input", rods)

def metres(rods):
    rods *= 5.0292
    
    return rods

    
def feet(f):
    f = x * 0.3048
    print(f)
    return(f)

def miles(m):
    m = x * 1609.34
    print(m)
    return(m)

def furlongs():
    h = rods / 40
    print(h)
    return(h)

x = metres(rods)
print(rods)
f = feet(x)
miles(m)
h = furlongs()


