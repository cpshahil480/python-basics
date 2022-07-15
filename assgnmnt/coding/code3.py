def add(n1,n2):
    print(n1+n2)
def sub(n1,n2):
    print(n1-n2)
def mult(n1,n2):
    print(n1*n2)
def div(n1,n2):
    print(n1/n2)
def flrdiv(n1,n2):
    print(n1//n2)
def expnt(n1,n2):
    print(n1**n2)


while True:
    m1=int(input("addition=1\nsubstraction=2\nmultiplication=3\ndivision=4\nfloor division=5\nexponent=6\nstop=7\nchoose your methode="))
    if m1==7:
        break
    elif m1 in (1,2,3,4,5,6):
        num1=float(input("enter first digit="))
        num2=float(input("enter second digit="))
        if m1==1:
            add(num1,num2)
        elif m1==2:
            sub(num1,num2)
        elif m1==3:
            mult(num1,num2)
        elif m1==4:
            div(num1,num2)
        elif m1==5:
            flrdiv(num1,num2)
        elif m1==6:
            expnt(num1,num2)
    else:
        print("invalid")

    print("...............")