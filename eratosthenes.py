import numpy as np

n = 100
x = np.ones([n, 1])
x[0] = 0

N = int(np.sqrt(n))

for i in range(2, N):
    for j in range(i+1, n+1):
        if j % i == 0:
            x[j-1] = 0

prime = 0;
for i in x:
    prime += 1
    if i == 1:
        print ("prime =", prime)
sum = int(np.sum(x))
print ("The sum of prime: ", sum)