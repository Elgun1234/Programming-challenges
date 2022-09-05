x = float(input("enter richter scale measurement "))

energy = pow(10, 1.5 * x +4.8)
tnt = energy / 4.184 * pow(10, 9)

print("equivalence in joules : ", energy)
print("equivalence in tons of tnt", tnt)
