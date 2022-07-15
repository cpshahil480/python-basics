#feb 01,1,2,3,5

def recfib(n):
    if n<=1:
        return n
    else:
        return recfib(n-1)+recfib(n-2)
    #            2+1

nterm=int(input("enter no of terms"))
for i in range(nterm):
    print(recfib(i))

#recfib()