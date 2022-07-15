class Student:
    def __init__(self,name,rollno,mark):
        self.name=name
        self.rollno=rollno
        self.mark=mark

    def printst(self):
        print(self.name,self.rollno,self.mark)

f=open('student.txt', 'r')
for i in f:
    data=i.rstrip('\n').split(",")
    name=data[0]
    rollno=data[1]
    mark=data[2]
    p=Student(name,rollno,mark)
    p.printst()