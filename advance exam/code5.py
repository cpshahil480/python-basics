#overriding
# same method name same number of arguments
# child class method overriding parent class method
class Book1:
    def books(self,name):
        self.name=name
        print(self.name,"cobol")

class Book2(Book1):
    def books(self,name):
        self.name=name
        print(self.name,"harry potter")

bk=Book2()
bk.books("")