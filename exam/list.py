lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
m=[]
[m.append(i) for i in lst if i not in m ]
print(m)