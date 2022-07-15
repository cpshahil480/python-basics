# multilevel inheritence
class A:
    def printa(self):
        print("inside a")
class B(A):
    def printb(self):
        print("inside b")

class C(B):
    def printc(self):
        print("inside c")

c=C()
c.printb()
c.printa()
c.printc()