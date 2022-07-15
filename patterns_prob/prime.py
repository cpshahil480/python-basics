n=int(input("enter a number"))
flag=0
for f in range(2,n):
    if n%f==0:

        flag=1
        break

if flag==0:
    print("prime")
else:
    print("not prime")