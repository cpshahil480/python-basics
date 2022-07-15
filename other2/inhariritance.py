class baseclass:
    def set_name(self,name):
        self.name=name





class subclass(baseclass):
    def welcome(self):
        print('welcome')


    def display_name(self):
        print(self.name)





y=subclass()
y.welcome()
y.set_name("dhs")
y.display_name()