#multiple inheritence

class A:
    def printa(self):
        print(" inside a")


class B:
    def printb(self):
        print("inside b")

class C(A,B):
    def printc(self):
        print("inside c")

s=C()
s.printa()
s.printb()
s.printc()
    