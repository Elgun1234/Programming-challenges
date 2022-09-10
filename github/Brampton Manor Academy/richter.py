def richter_input():
    richter = float(input("\nenter richter scale measurement: "))
    return richter

def joule_converter(x):
    joule = pow(10,1.5*x+4.8)
    return joule
    
 
def tnt_converter(joule):
    tnt = joule / pow(10,9)*4.184
    return tnt


richter_j_1 = joule_converter(1)
richter_t_1 = tnt_converter(richter_j_1)

richter_j_5 = joule_converter(5)
richter_t_5 = tnt_converter(richter_j_5)

richter_j_9_1 = joule_converter(9.1)
richter_t_9_1 = tnt_converter(richter_j_9_1)

richter_j_9_2 = joule_converter(9.2)
richter_t_9_2 = tnt_converter(richter_j_9_2)

richter_j_9_5 = joule_converter(9.5)
richter_t_9_5 = tnt_converter(richter_j_9_5)

r = "Richters"
j = "Joules"
t = "Tons of TNT"

print(f"{r:21}{j:36}{t}\n")
print(f"{1:4} {richter_j_1:28} {richter_t_1:40}")
print(f"{5:4} {richter_j_5:28} {richter_t_5:38}")
print(f"{9.1:5} {richter_j_9_1:30} {richter_t_9_1:36}")
print(f"{9.2:5} {richter_j_9_2:30} {richter_t_9_2:36}")
print(f"{9.5:5} {richter_j_9_5:31} {richter_t_9_5:34}")

richter = richter_input()    
joule = joule_converter(richter)
tnt = tnt_converter(joule)

print(f"Richter value: {richter}")
print(f"equivalence in joules: {joule}")
print(f"equivalence in Tons of TNT: {tnt}")
