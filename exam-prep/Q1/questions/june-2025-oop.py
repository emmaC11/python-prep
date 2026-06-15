class Vehicle:
    vCount = 0 # class var
    def __init__(self, reg, department):
        self.reg = reg # instance var
        self.department = department # instance var
        self._itinerary = ['stop 1', 'stop 2', 'stop 3'] # protected
        Vehicle.vCount += 1

    def display(self):
        itinerary_string = ','.join(self._itinerary) 
        print(f'Vehicle with reg {self.reg}, in the department of {self.department} has {itinerary_string} on their current itinerary.')

    def addStop(self,loc):
        self._itinerary.append(loc)

class Truck(Vehicle):
    def __init__(self, reg, department, payload):
        super().__init__(reg, department)
        self.payload = payload

    def display(self):
        super().display()
        print(f'payload is {self.payload}')

v = Vehicle('2024', 'dept')
v.addStop('new stop')
v.display()

t = Truck('2024', 'dept', 'payload')
t.display()

