
a = 4416
b = 9387
summe = 0

for x in range(a, b+1):
    if x % 2 == 0:
        continue
    else:
        summe = (summe + x)

print(summe)



