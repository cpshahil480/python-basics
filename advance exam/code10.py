import re
n=input("enter string")
rule='[A-Z][a-z\W]*'
match=re.fullmatch(rule,n)
if match is not None:
    print("valid")
else:
    print("invalid")