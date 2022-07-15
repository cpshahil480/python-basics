s=input("enter a string")
count={}
m=s.split(" ")

# for i in m:
#     if i not in count:
#         count.update({i:1})
#
#     else:
#         val=count[i]
#         val=val+1
#         count.update({i:val})
# print(count)

for i in m:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1

print(count)