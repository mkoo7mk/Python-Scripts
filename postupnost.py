import random

a = [x + random.randint(x + 1, 2*x) for x in range(1, 101)]
s = 0
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] + a[j] % 100 == 0:
            print(a[i], "||||", a[j])
            s += 1
print(s)