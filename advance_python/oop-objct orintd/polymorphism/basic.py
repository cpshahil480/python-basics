#polymorphism
#1.method overloading
#2.method overriding


#overloading
# same methode name diff num of argmnts  ee methodil arguments noki print cheyum
class A:
    def printa(self,num1):
        self.num1=num1
        print(self.num1,"inside a")
class B(A):
    def printa(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1,self.num2,"inside b")

b=B()
b.printa(5)#class a method
b.printa(5,8)#class b method   now python dont support this but thearatically asking

