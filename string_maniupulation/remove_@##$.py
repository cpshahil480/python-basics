s=input("enter string")
symbols=("+!@#$%^&*()-_=+{}[]:;'?")
b=""

for i in s:
    if i not in symbols:
        b=b+i
print(b)        