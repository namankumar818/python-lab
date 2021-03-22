a = int(input('enter the number:-'))
i = 2
while i < a:
    if a%i == 0:
        print('not prime')
        break
    i += 1
else:
    print("prime")
