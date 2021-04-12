a = int(input('enter the number'))
b = int(input('enter the number'))
c = int(input('enter the number'))
d = b*b
e = 4*a*c
f = d - e
if f > 0:
    print('real roots')
elif f == 0:
    print("equal roots")
else:
    print("not real roots")
