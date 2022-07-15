import re
n=input("enter a word")
x='[a-z0-9._]+[@][a-z]+[.][comin]{2,3}'
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")