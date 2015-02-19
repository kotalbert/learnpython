# Animal class
class Animal(object):
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def description(self):
        print self.name
        print self.age
        print self.is_alive

hippo = Animal("Tim", 18)
hippo.description()
hippo.is_alive = False
hippo.description()