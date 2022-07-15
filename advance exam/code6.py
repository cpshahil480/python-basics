class Student:
    def __init__(self,name,rollno,degree,mark):
        self.name=name
        self.rollno=rollno
        self.degree=degree
        self.mark=mark

    def printa(self):
        print(self.name,self.rollno,self.degree,self.mark)

f=open('student.txt','r')
for i in f:
    data=i.rstrip("\n").split(",")
    name=data[0]
    rollno=data[1]
    degree=data[2]
    mark=data[3]
    for j in mark:
        if j>190:
            print(j)

    # pa=Student(name,rollno,degree,mark)
    # pa.printa()
