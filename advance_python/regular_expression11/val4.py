import re
n=input("enter a word")
x='[A-Z]*[\d\W]'
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")