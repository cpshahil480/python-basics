l=[3,6,1,7,0,8,2,4]

newlist=[]
while l:   #check l elementg
    minimum=l[0]# take minimum element l[0]
    for i in l:  #iterate l
        if i<minimum: #3<3,1<3
            minimum=i  #1

    newlist.append(minimum)
    l.remove(minimum)
print(newlist)