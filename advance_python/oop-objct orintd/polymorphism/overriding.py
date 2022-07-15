#overriding
# same method name same number of arguments
# child class method overriding parent class method

class A:
    def printa(self,num1):
        self.num1=num1
        print(self.num1,"inside a")
class B(A):
    def printa(self,num1):
        self.num1=num1

        print(self.num1,"inside b")

b=B()
b.printa(6)