class Vehicle:
    def __init__(self,model_name,colour):
        self.model_name=model_name
        self.colour=colour

    def printcar(self):
        print(self.model_name,self.colour)


class Bus(Vehicle):
    def __init__(self,model_name,colour,model,year):
        super(Bus, self).__init__(model_name,colour)
        self.model=model
        self.year=year

    def printvehicle(self):
        print(self.model,self.year,self.model_name,self.colour)

p1=Bus("volvo","red","sleeper",2010)
p1.printvehicle()