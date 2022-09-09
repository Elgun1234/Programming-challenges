import time
x = int(input("find sum of numbers from 1 to "))
start = time.time()
z = x
z += 1
x *= z
x /= 2
end = time.time()
print((end-start)*10**3, "ms")
print(x)
