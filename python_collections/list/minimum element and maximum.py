l=[3,6,1,7,0,8,2,4]

newlist=[]
while l:
    minimum=l[0]
    for i in l:
        if i<minimum:
            minimum=i

    newlist.append(minimum)
    l.remove(minimum)
print("minimum element",newlist[0])
print("maximum element",newlist[-1])