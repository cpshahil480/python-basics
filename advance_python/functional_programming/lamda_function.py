#lamda function

def add(n1,n2):
    return n1+n2

print(add(5,6))

#another mthd

add=lambda n1,n2:n1+n2
print(add(3,4))
check=lambda n:n>0
print(check(5))

# n1=input("enter word")
# first=lambda n1:n1[0]
# print(first(n1))

palindrom=lambda s:s[::-1]
print(palindrom("swift"))
