class bike(object):

    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print 'Price is: $' + str(self.price)
        print 'Maximum speed' + str(self.max_speed)
        print 'Total Miles' + str(self.miles)

    def ride(self):
        print 'Riding' 
        self.miles += 10

    def reverse(self):
        print 'Reversing'
        if self.miles >= 5:
            self.miles -=5

bike1 = bike(100, 20)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = bike(200,10)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = bike(150,30)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()


