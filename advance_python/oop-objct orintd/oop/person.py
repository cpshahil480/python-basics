class Person:
    def setvalue(self,name,age,place):
        self.firstname=name
        self.age=age
        self.place=place

    def printvalue(self):
        print(self.firstname)
        print(self.age)
        print(self.place)


pe1=Person()
pe1.setvalue("shahil",20,"puthanathani")
pe1.printvalue()
pe2=Person()
pe2.setvalue("aju",23,"clct")
pe2.printvalue()