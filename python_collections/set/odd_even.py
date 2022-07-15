s1={1,5,7,9,4,3,6,77,45,33,94,63}
odd=set()
even=set()
for i in s1:
    if i%2==1:
        odd.add(i)
    elif i%2==0:
        even.add(i)


print("odd=",odd)
print("even=",even)