def recsum(n):
    if n==0:
        return n
    else:
        return n+recsum(n-1)

print(recsum(3))

