f=0
for i in range(5):
    for k in range(f):
        print(" ",end=" ")
    f=f+1

    for j in range(5-f):
        print("*",end="   ")
    print()