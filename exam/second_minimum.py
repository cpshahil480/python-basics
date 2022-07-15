lst=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
m=[]
for i in lst:
    if i not in m:
        m.append(i)

m.sort()
print(m[1])