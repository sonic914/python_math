import numpy as np

n = 100
x = np.ones([n, 1])
x[0] = 0

for i in range (2, n+1):
    for j in range (2, i):
        if i % j == 0:
            x[i-1] = 0
            break
print (x)

prime = 0
count = 0
for i in x:
    prime += 1
    if i == 1:
        count += 1
        print (count, "-> prime= ", prime)
