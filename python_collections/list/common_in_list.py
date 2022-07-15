l=[1,2,3,4,6,1,2,3]
m=[]
n=[]
for i in l:
    if i not in m:
        m.append(i)

    else:
        n.append(i)


print(n,m)
