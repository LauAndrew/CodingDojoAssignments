class animal(object):

    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        print 'walking'
        self.health -= 1
        return self
    
    def run(self):
        print 'runnning'
        self.health -= 5
        return self
    
    def display_health(self):
        # print 'My name is: '+ str(self.name)
        print 'Health:' +str(self.health)
        return self



class dog(animal):
    def __init__(self,name):
        super(dog, self).__init__(name)
        self.health = 150
    
    def pet(self):
        self.health += 5
        return self

class dragon(animal):
    def __init__(self,name):
        super(dragon, self).__init__(name)
        self.health = 170
    
    def fly(self):
        self.health -= 10
        print "I am a Dragon"
        return self


pet1 = dog(animal)
pet1.walk().walk().walk().run().run().pet().display_health()

pet2 = dragon(animal)
pet2.walk().walk().walk().run().run().fly().display_health()