class Parent:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone

    def printpa(self):
        print(self.name,self.phone)

f=open('parent.txt', 'r')
for i in f:
    data=i.rstrip('\n').split(",")
    name=data[0]
    phn=data[1]
    pa=Parent(name,phn)
    pa.printpa()