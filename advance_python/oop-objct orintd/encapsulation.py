#encapsulation
class A:
    def __init__(self):
        self.a=1 #public
        self._b=2 #protected
        self.__c=3#private cls inside ninum private vrble accss ahnu elathathu accs patila

    def display(self):
        print(self.__c)



a=A()
print(a.a,a._b,)
a.display()