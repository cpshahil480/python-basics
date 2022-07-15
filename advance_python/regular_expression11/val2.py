# import re
# n=input("enter a word")
# x='[a][\w\W]*[b]'
# matcher=re.fullmatch(x,n)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")
# + MINIMUM ONE CHARACTER * 0-INFINITE CHARACTER

import re
n=input("enter word")
x='\d{2}[\W]+'
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")
