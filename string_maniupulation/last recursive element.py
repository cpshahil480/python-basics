n="abcab"
e=""
f=""
for i in n:
    if i not in e:
        e=e+i

    else:
        f=f+i
print("last recursive",f[-1])
