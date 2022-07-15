l=[5,9,1,8,2,7,3,4,6]
e=int(input("enter element to search"))
l.sort()
flag=0
low=0
upper=len(l)-1
while low<=upper:
    mid=(low+upper)//2
    if l[mid]==e:
        flag=1
        break
    elif e>l[mid]:
        low=mid+1
    elif e<l[mid]:
        upper=mid-1

if flag==1:
    print("found")
else:
    print("not found")


