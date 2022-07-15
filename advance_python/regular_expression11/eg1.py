
import re
count=0
x='[^abc]'
matcher=re.finditer(x,'hsavcdaVBBSAHD')
for i in matcher:
    print(i.start())
    print(i.group())
    count=count+1

print("total=",count)