s=input("enter string")#ambrala
v="aeiou"
new=""
for i in s:
    if i not in v:
        new=new+i

print(new)
