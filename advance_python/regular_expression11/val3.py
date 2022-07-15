# import re
# n=input("enter a word")
# x='[A-Z\d]{3,8}'
# matcher=re.fullmatch(x,n)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")
#


import re
n=input("enter a word")
x='[a][a-z]{3,8}[a]'
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")