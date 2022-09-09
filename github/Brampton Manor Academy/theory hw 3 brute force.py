import time
n = int(input("find sum of numbers from 1 to "))
start = time.time()
x = 0
for i in range(1,n+1):
    x += i
    

end = time.time()
print((end-start)*10**3, "ms")
print(x)
