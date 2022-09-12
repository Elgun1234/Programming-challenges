def order():
    x = str(input("enter letter "))
    x = x.lower()
    x = ord(x)
    x-=96
    return x

x = order()

if x == 1:
    print(f"{x}st")
if x == 2:
    print(f"{x}nd")
if x == 3:
    print("{x}rd")
else:
    print(f"{x}th")









