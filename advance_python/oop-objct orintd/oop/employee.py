#self is used to point to the current instance
#instance.......related to methods.....self
#static......related to class.......class name
class Employee:
    company_name="luminar"
    def setemply(self,name,id,designation,salary):
        self.name=name
        self.id=id
        self.designation=designation
        self.salary=salary


    def setprint(self):
        print("name=",self.name)
        print("id=",self.id)
        print("desig=",self.designation)
        print("salary=",self.salary,Employee.company_name)



em1=Employee()
em1.setemply("shahil",123,"hr",100000)
em1.setprint()
print("..................")
em2=Employee()
em2.setemply("sibin",124,"hr",100000)
em2.setprint()











