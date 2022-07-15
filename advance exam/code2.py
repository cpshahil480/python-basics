class Person:
    collage="luminar"
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Employee(Person):
    def setemployee(self,id,designation,salary):
        self.id=id
        self.designation=designation
        self.salary=salary
    def selfprnt(self):
        print(self.id,self.designation,self.salary,self.name,self.age,self.place,Person.collage)



p1=Employee()
p1.setemployee(12,"hr",100000)
p1.setperson("shahil",12,"puth")
p1.selfprnt()
p2=Employee()
p2.setperson("sibin",23,"cheru")
p2.setemployee(13,"ai",100000)
p2.selfprnt()