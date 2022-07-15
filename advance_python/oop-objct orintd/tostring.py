class Person:
    def setvalue(self,name,age,place):
        self.firstname=name
        self.age=age
        self.place=place

    def printvalue(self):
        print(self.firstname)
        print(self.age)
        print(self.place)

    def __str__(self):
        return self.firstname+self.place+str(self.age)



pe1=Person()
pe1.setvalue("anu",12,"kochi")
print(pe1)

#convrt reference into str
