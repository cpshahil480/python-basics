class Person:
    def setper(self,name,age ,place):
        self.name=name
        self.age=age
        self.place=place

        print(self.name,self.age,self.place)

class Parent:
    def setpar(self,phone,adress):
        self.phone=phone
        self.adress=adress

        print(self.phone,self.adress)

class Employee(Person,Parent):
    def setemp(self,id,des,salary):
        self.id=id
        self.das=des
        self.salar=salary

        print(self.id,self.das,self.salar)



m=Employee()
m.setpar("shahil",12,)
m.setemp(321,"cherey","per")
m.setper(12,"mala",10000)
