class kettle(object):

    powerSourse="Electricity"
    
    def __init__(self,make,price):
        self.make=make
        self.price= price
        self.on=False

    def switchOn(self):
        self.on=True

kenwood=kettle("kenwoodzzz",96)
print(kenwood.make)

hamilton=kettle("xamilton",00)
hamilton.price=5.99

print(hamilton.price)

print(  "Models: {0.make} =Price: {0.price},{1.make} =Price: {1.price}".format(kenwood,hamilton))

hamilton.switchOn()

print(hamilton.on)
kettle.switchOn(kenwood)
print(kenwood.on)

print("z"*40)

kenwood.power=1.5
print(kenwood.power)
print(kenwood.__dict__)
print(kettle.powerSourse,kenwood.powerSourse)
kenwood.powerSourse="gas"
print(kenwood.powerSourse)
print(kettle.__dict__)
print(kenwood.__dict__)

