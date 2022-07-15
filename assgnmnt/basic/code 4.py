def sum_odd(num1,num2):
    sum=0
    for i in range(num1,num2+1):
        if i%2==1:
            sum=sum+i
    print(sum)

n1=20
n2=30
sum_odd(n1,n2)
