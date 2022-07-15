import re
n=input("enter string")
rule='[a]{5}[b]'
match=re.fullmatch(rule,n)
if match is not None:
    print("valid")
else:
    print("invalid")