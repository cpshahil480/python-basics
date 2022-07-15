class Person:
    def __init__(self,name,age ,place):
        self.name=name
        self.age=age
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place)

class Parent:
    def __init__(self,phone,adress):
        self.phone=phone
        self.adress=adress
    def printpar(self):
        print(self.phone,self.adress)

class Employee(Person,Parent):
    def __init__(self,id,des,salary,name,age,place,phone,adress):
        Person.__init__(self,name,age,place)
        Parent.__init__(self,phone,adress)
        self.id=id
        self.das=des
        self.salar=salary
    def printemp(self):
        print(self.id,self.das,self.salar)


emu=Employee(1,"DEV",6700,"amal",27,"kochi","abc",9562693350)
emu.printemp()
emu.printpar()
emu.printper()