class Student:
    place="puth"
    def __init__(self,name,cls,age):
        self.name=name
        self.cls=cls
        self.age=age

    def printstu(self):
        print(self.name,self.cls,self.age,Student.place)
name=input("enter name")
st1=Student(name,1,"cs")
st1.printstu()
print(st1.name,st1.cls,st1.place)