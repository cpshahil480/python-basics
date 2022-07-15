f=open('excample.py','r')
for i in f:
    data=i.rstrip("\n")#for avoiding space btwn string
    print(data)