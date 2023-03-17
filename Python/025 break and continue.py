#break statement breaks out of the loop immediately

for i in range(1,101):
    if i % 5 == 0:
        break
    else:
        print(i)

# continue -> skips that iteration

# all numbers from 1 to 100 without the multiples of 5

for i in range(1,101):
    if i%5==0:
        continue
    else:
        print(i)

