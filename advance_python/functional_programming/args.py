#args-arguments
def printnumbers(*args):
    print(args)

printnumbers(3,4,5,6)

#*args tuple..name=args(u can give any name)



def sum(*n):
    sum=0
    for i in n:
        sum=sum+i

    print(sum)

sum(1,2,3,4)
sum(12,23)