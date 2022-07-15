s="luminar technolab"
e=input("enter a word")
new=""


for i in s:
    if i not in e:
        new=new+i
print(new)
