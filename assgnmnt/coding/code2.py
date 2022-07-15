initial=int(input("enter initial element"))
final=int(input("enter final number"))
sum=0
for i in range(initial,final):
    for j in range(2,i):
        if i%j==0:
            break

    else:
        sum=sum+i

print(sum)
