target = 5000
count = 1
test = 3
answer = 0

while count < target-1:
    test += 2
    is_prime = 1
    for i in range (2, test):
        if test % i == 0:
            is_prime = 0
            break
    if (is_prime):
        answer = test
        count += 1

print (answer)       