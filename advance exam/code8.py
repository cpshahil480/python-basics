#try:
#except:
#finally=finally work always

num1=int(input("enter n1"))
num2=int(input("enter n2"))

try:
    print("hi")
    print(num1/num2)
except:
    print("error")
finally:
    print("in finally")