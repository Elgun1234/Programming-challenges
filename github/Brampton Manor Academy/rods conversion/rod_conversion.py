def rods_input():
    rods = float(input("rods "))
    print(f"your input {rods}")
    return rods

def metres(rods):
    rods_to_metres = rods / 5.0292 
    print(f"metres: {rods_to_metres}")
    return rods_to_metres

    
def feet(rods_to_metres):
    metres_to_feet = rods_to_metres * 0.3048 
    print(f"feet: {metres_to_feet}")
    return metres_to_feet

def miles(rods_to_metres):
    metres_to_miles = rods_to_metres * 1609.34
    print(f"miles: {metres_to_miles}")
    return metres_to_miles

def furlongs(rods):
    rods_to_furlongs = rods / 40
    print(f"furlongs: {rods_to_furlongs}")
    return(rods_to_furlongs)

def walkspeed(rods_to_metres):
    ws = rods_to_metres / 60
    print(f"walkspeed: {ws}")
    return ws
if __name__ == "__main__":
    rods = rods_input()
    rods_to_metres = metres(rods)
    metres_to_feet = feet(rods_to_metres)
    metres_to_miles = miles(rods_to_metres)
    rods_to_furlongs = furlongs(rods)
    ws = walkspeed(rods_to_metres)














