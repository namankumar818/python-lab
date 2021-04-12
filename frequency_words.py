st = input("enter the string:- ")
reg = ''
for i in st:
    if i not in reg:
        reg += i
        print(f'{i}:{st.count(i)}')
