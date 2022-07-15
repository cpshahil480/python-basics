
# import re
# count=0
# x='[a-z]'
# matcher=re.finditer(x,'hsavcdaVBBSAHD')
# for i in matcher:
#     print(i.start())
#     print(i.group())
#     count=count+1
#
# print("total=",count)


import re
count=0
x='[\W]'
matcher=re.finditer(x,'hsavcdaV BB$%^$#4SAHD')
for i in matcher:
    print(i.start())
    print(i.group())
    count=count+1

print("total=",count)