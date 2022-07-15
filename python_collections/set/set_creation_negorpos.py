s={1,4,7,8,-9,22,-55,11,-7}
pos=set()
neg=set()
for i in s:
    if i>0:
        pos.add(i)
    elif i<0:
        neg.add(i)
print(pos)
print(neg)