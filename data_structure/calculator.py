def add(n1,n2):
    if n==1:
        print(n1+n2)
def sub(s1,s2):
    if n==2:
        print(n1-n2)
def mult(m1,m2):
    if n==3:
        print(n1*n2 )
def div(l1,l2):
    if n==4:
        print(n1/n2)
def error(n):
        print("invalid")
def stop(n):
        print("stop")







print("1=addition\n2=for substraction\n3=multiplication\n4=division\n5=stop")


while True:
    n = int(input("select operation"))

    if n==5:
        stop(n)
        break
    if n>=6:
        error(n)


    #n = int(input("select operation"))




    n1=float(input("num1="))
    n2=float(input("num2="))


    add(n1,n2)
    sub(n1,n2)
    mult(n1,n2)
    div(n1,n2)

