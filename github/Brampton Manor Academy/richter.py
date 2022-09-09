def richter_input():
    richter = float(input("enter richter scale measurement: "))
    return richter

def converter(x):
    joule = pow(10,1.5*x+4.8)
    tnt = joule / pow(4.184*10,9)
    if x == richter:
        print(f"your richter value {x}")
    else:
        print(f"richter: {x}")
    print(f"equivalence in joules: {joule}")
    print(f"equivalence in tnt: {tnt}")
    



richter = richter_input()
converter(1)
converter(5)
converter(9.1)
converter(9.2)
converter(9.5)
converter(richter)
