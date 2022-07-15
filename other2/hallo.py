num1=int(input("enter first number = "))
num2=int(input("enter second number = "))

print("1 for addition\n2 for substraction\n3 for division")

num3=int(input("select your method = "))


if num3==1:
    print("result=",num1+num2)

elif num3==2:
    print("result=",num1-num2)
elif num3==3:
    print("result=",num1/num2)
else:
    print("invalid")


print("***thankyou***")

