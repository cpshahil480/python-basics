def add(n1,n2):
        print(n1+n2)
def subn(n1,n2):
        print(n1-n2)
def mult(n1,n2):
        print(n1*n2 )
def div(n1,n2):
        print(n1/n2)


while True:
    choose=int(input("choose method\n1=add\n2=substraction\n3=multiplication\n4=division\n5=stop"))
    if choose==5:
        break
    elif choose in (1,2,3,4,):
        num1=float(input("enter num1"))
        num2 = float(input("enter num2"))
        if choose==1:
            add(num1,num2)
        elif choose==2:
            sub(num1,num2)
        elif choose==3:
            mult(num1,num2)
        elif choose==4:
            div(num1,num2)
    else:
        print("invalid")


