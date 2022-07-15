s="hello hi hello"
count={}
d=s.split(" ")
for i in d:
    if i not in count:
        count.update({i:1})

    else:
        val=count[i]
        val=val+i
        count.update({i:val})
print(count)