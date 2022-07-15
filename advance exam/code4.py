class Animal:
    def __init__(self,category,gender):
        self.category=category
        self.gender=gender


class Dog(Animal):
    def __init__(self,breed,colour,category,gender):
        super(Dog, self).__init__(category,gender)
        self.breed=breed
        self.colour=colour

    def printli(self):
        print(self.breed,self.colour,self.category,self.gender)

anim=Dog("bull dog","brown","dog","male")
anim.printli()