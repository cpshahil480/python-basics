import re
# phn=input("enter your number to validate")
# rule='[+][9][1]\d{10}'
# matcher=re.fullmatch(rule,phn)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")



no=input("enter vehicle number")
rule='[K][L]\d{2}[A-Z]\d{4}'
match=re.fullmatch(rule,no)
if match is not None:
    print("valid")
else:
    print("invalid")