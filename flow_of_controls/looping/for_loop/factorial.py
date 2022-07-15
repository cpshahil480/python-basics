#factorial 1*2*3*4 1*2=2 2*3=6

n=int(input("enter a number"))
fact=1
for x in range(1,n+1):
    fact=fact*x

print(fact)
        