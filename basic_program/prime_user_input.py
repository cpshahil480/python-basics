m=int(input("enter initial"))
s=int(input("enter final"))


for i in range(m,s):
    for j in range(2,i):
        if i%j==0:
            break

    else:
        print(i)