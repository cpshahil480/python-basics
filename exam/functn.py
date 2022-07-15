
def sum_of_odd(n1,n2):
    sum=0
    for i in range(n1,n2+1):
        if i%2==1:
            sum=sum+i
    return sum



print(sum_of_odd(40,80))
#sum_of_odd(n1,n2)