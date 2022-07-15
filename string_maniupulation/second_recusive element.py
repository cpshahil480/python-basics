n="aaabbbccc"
e=""
rec=""
for i in n:
    if i not in e:
        e=e+i
    elif i not in rec:
        rec=rec+i

print(rec[1])