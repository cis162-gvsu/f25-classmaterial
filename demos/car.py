class Car:

    # constructor
    def __init__(self, ndoors, color, numseats, make, model, year):
        self.ndoors = ndoors
        self.color = color
        self.numseats = numseats
        self.make = make
        self.model = model
        self.year = year
        self.on = False
        self.speed = 0
        self.direction_idx = 0
        self.gear = 'P'
        self.position = [0,0]

    def get_direction(self):
        carddir = ['N','W','S','E']
        return carddir[self.direction_idx]

    def start(self):
        self.on = True

    def accelerate(self, rate):
        self.speed += rate

    def turn(self, turndir):
        if turndir == 'left':
            self.direction_idx += 1
            #self.direction_idx = self.direction_idx % 4
            if self.direction_idx == 4:
                self.direction_idx = 0

        if turndir == 'right':
            self.direction_idx -= 1
            if self.direction_idx == -1:
                self.direction_idx = 3

    def change_gear(self, gear):
        self.gear = gear
    
    def move(self):
        if self.direction_idx == 0:
            self.position[1] += self.speed
        if self.direction_idx == 1:
            self.position[0] -= self.speed
        if self.direction_idx == 2:
            self.position[1] -= self.speed
        if self.direction_idx == 3:
            self.position[0] += self.speed

    def __str__(self):
        

# instantiating the Car class -> calls constructor
mycar = Car(4, 'red', 5, 'toyota', 'camry', 2016)

mycar.change_gear('D')
print(mycar.get_direction())
print(mycar.speed)
mycar.accelerate(10)
print(mycar.speed)
x = str(mycar)
print(x)

