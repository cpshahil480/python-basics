#inheritence
#child class consist 1 element is called single inheritence
class A:  #parent class/base class/super class
    def printa(self):
        print("inside a class")
class B(A): #child class/sub class/derived class
    def printb(self):
        print("inside b class")


b=B()
b.printb()
b.printa()