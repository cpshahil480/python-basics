#function
def sum():
    n1=int(input("enter no1"))
    n2=int(input("enter no2"))
    print(n1+n2)
sum()
#function with argument
def sum(n1,n2):
    print(n1+n2)
sum(1,3)
#function with argument and return type
def sum(n1,n2):
    return n1+n2

print(sum(1,3))

