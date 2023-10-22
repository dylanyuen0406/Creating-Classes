class car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, increase):
        self.speed += increase
        print("The"+self.make+self.model+"is now going"+str(self.speed)+"km/h")

    def brake(self, increase):
        self.speed -= increase
        print("The" + self.make + self.model + "is now going" +str(self.speed) + "km/h")





var1 =car("Honda","Civic", 1900, 25)
var2 = car('Hyundai',"Avante",1234,40)
var1.accelerate(20000)
var2.brake(38)