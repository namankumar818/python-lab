a = input("enter the string :- ")
v = 0
d = 0
s = 0
c = 0
for i in a:
    if i == 'A' or i == 'a' or i == 'E' or i == 'e' or i == 'i' or i == 'I' or i == 'o'or i == 'O' or i == 'u' or i == 'U':
        v += 1
    elif '0' < i <= '9':
        d += 1
    
    elif i == ' ':
        s += 1
    else:
        c += 1

print('the vovels are :-',v)
print('the digits are :-',d)
print('the white spaces are :-',s)
print('the consonants are :-',c)
