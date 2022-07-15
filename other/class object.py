class teamMembers:
    year=2020
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def add_age(self,):
        self.age=self.age+1

    def relocate(self,place):
        self.place=place

    def display(self):
        print("year :"+str(teamMembers.year))
        print("name :"+self.name)
        print("age :"+str(self.age))
        print("place :"+self.place)

    @classmethod
    def add_year(cls):
        cls.year=cls.year+1

    @staticmethod
    def display_welcome():
        print("welcome")

print("*****\n"
      " ***\n"
      "  *")

teamMembers.display_welcome()

x=teamMembers("shahil",21,"puth")
y=teamMembers("sibin",23,"calicut")

x.display()
y.display()

print('------------------')
teamMembers.year=teamMembers.year+1

x.add_age()
y.add_age()

x.display()
y.display()



print('------------------')
teamMembers.add_year()


x.add_age()
y.add_age()

x.relocate("andra")
y.relocate("assam")

x.display()
y.display()