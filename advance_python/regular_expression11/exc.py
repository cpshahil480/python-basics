# import re
# count=0
# matcher=re.finditer('ab','abaaaaaaaaabab')
# for i in matcher:
#     print(i.start())
#     print(i.group())
#     count=count+1
#
# print(count)

#start=position of ab
#group=which group we are matching

import re
count=0
x='[^abc]'
matcher=re.finditer(x,'hsavcdaVBBSAHD')
for i in matcher:
    print(i.start())
    print(i.group())
    count=count+1

print("total=",count)