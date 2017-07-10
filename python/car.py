class car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()
    
    def display_all(self):
        print 'Price:' +str(self.price)
        print 'Speed:' +str(self.speed)
        print 'Fuel:' +str(self.fuel)
        print 'Mileage:' +str(self.mileage)
        print 'Tax:' +str(self.tax)

car1 = car(20000,20,10,60)
car2 = car(9000, 50, 100, 80)
car3 = car(6000, 40, 50, 90)
car4 = car(30000, 50, 50, 70)
car5 = car(76000, 70, 10, 10)
car6 = car(300000, 20, 70, 40)