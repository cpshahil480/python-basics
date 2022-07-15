def recsum(n):
    if n==0:
        return n
    else:
        return n+recsum(n-1)
              #3+recsum(3-1=2)=6
              #2+recsum(2-1=1)=3
              #1+recsum(1-1=0)=1
print(recsum(3))