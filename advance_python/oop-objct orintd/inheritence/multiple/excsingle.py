class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
         print(self.name,self.age,self.place)

class Student(Person):
    def setstudents(self,roll,dpt,school):
        self.roll=roll
        self.dpt=dpt
        self.school=school
    def printstudent(self):
        print(self.roll,self.dpt,self.school,self.name,self.age,self.place)

st=Student()
st.setvalue("anu",12,"puth")
st.setstudents(1,"cse","luminar")
st.printstudent()


#person employee relation