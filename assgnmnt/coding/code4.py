n1=input("enter a word")
n2="aeiou"
n3=""

for i in n1:
    if i not in n2:
        n3=n3+i

print(n3)

