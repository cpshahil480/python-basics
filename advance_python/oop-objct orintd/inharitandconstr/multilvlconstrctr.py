class Person:
    def __init__(self,name,age ,place):
        self.name=name
        self.age=age
        self.place=place

        print(self.name,self.age,self.place)

class Parent(Person):
    def __init__(self,phone,adress,name,age ,place):
        super(Parent, self).__init__(name,age, place)
        self.phone=phone
        self.adress=adress

        print(self.phone,self.adress)

class Employee(Parent):
    def __init__(self,id,des,salary,phone,adress,name,age ,place):
        super(Employee, self).__init__(phone, adress, name, age, place)
        self.id=id
        self.das=des
        self.salary=salary

    def printemp(self):

        print(self.id,self.das,self.salary,self.phone,self.adress,self.name,self.age,self.place)

l1=Employee(1,"df",65000,3564524,"asd","shahil",13,"puth")
l1.printemp()