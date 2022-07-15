n=input("enter a word") #abcab
e=""
for i in n:
    if i not in e:
        e=e+i

    else:
        print("first recursive element",i)
        break

