import re
n=input("enter string")
rule='[A-Z]\w{4,9}[A-Z]'
match=re.fullmatch(rule,n)
if match is not None:
    print("valid")
else:
    print("invalid")