#prime
#2 prime
#1,2

#3 prime
#1,2

#4
# 124

#5prime
#15

#
#6
#1236
n=int(input("enter a num"))#5
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1


if flag==0:
    print("prime")
else:
    print("not prime")


