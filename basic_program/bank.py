fixed_amount=100000
sub=int(input("enter your withdraw amount ="))

if sub<fixed_amount:
    print(" avilable balance= ",fixed_amount-sub)

else:
    print("insufficient balance")