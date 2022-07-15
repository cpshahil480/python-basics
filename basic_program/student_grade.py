n1=float(input("enter your score = "))
if n1>=101:
    print("invalid")
elif n1>90:
    print("grade=A+")
elif n1>=80:
    print("grade=A")
elif n1>=70:
    print("grade=B")
elif n1>=60:
    print("grade=C")
elif n1>=50:
    print("grade=D")

else:
    print("failed")