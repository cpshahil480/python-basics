class Person:
    collage="luminar"
    def __init__(self,name,age,place1):
        self.name=name
        self.age=age
        self.place1=place1

class Employee(Person):
    def __init__(self,id,designation,salary,name,age,place1):
        super(Employee, self).__init__(name,age,place1)
        self.id=id
        self.designation=designation
        self.salary=salary
    def selfprnt(self):
        print(self.id,self.designation,self.salary,self.name,self.age,self.place1,Person.collage)

st1=Employee(1,"WER",100000,"shahil",12,"puth")
st1.selfprnt()