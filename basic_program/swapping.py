num1=10
num2=5
num3=num1
num1=num2
num2=num3


print("before swapping num1=",num1)
print("before swapping num2=",num2)

print(".......")

#method 2
num1=10
num2=5
num1,num2=num2,num1
print("after swapping num1=",num1)
print("after swapping num2=",num2)

print(".........")

#method3
a=10
b=5
a=a+b
b=a-b
a=a-b

print("after swapping num1=",a)
print("after swapping num2=",b)
