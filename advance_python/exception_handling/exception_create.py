#raise exception
age=int(input("enter age"))
if age<18:
    raise Exception("not eligible")
else:
    print("eligible")