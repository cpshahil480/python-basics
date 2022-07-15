#3 3*2*1  =6 fact

def recfact(n):
    if n==1:
        return n
    else:
        return n*recfact(n-1)
             #3*

print(recfact(3))