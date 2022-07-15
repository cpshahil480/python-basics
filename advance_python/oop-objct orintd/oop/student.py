class Student:
    school_name="luminar"
    def setstudent(self,name,roll_no,dpt):
        self.name=name
        self.roll_no=roll_no
        self.dpt=dpt

    def setprint(self):
        print(self.name)
        print(self.roll_no)
        print(self.dpt)
        print(Student.school_name)

dp1=Student()
dp1.setstudent("shahil",13,"mech")
dp1.setprint()

dp2=Student()
dp2.setstudent("raja",43,"civil")
dp2.setprint()

#employee name id designation salary cmpy name