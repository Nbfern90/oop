class User:  # Like a factory, provides default behavior and able to create objects,bluprints
    # if a class belongs to another class, it is written as: class= Child(Parent)

    # class attribute,definded outside of any instance method, we can #change them on an instance or an entire class: User.bank_name= "New Bank"   print(nick.bank_name) output= New Bank
    bank_name = "First National Dojo"

    # "Magic Method" called when a new object is #created,first #parameter and the instance attribute(characteristic shared by all #instances in class type)    We pass arguments(name,email_address) to specify a #user's instance attributes:
    def __init__(self, name, email_address):

        self.name = name  # these are our a
        self.email_address = email_address
        self.acount_balance = 0

    def make_deposit(self, amount):
        self.account_balance = + amount


# INSTANCES or OBJECTS added to the class
nick = User("Nick Fernandez", "Nick@gmail.com")
bob = User("Bob Johnson", "Bob@yahoo.com")

nick.name = "Nick"  # used to set values for out instance attributes


class Car:

    all_cars = []
    year = 2020  # class attribute -targets all the classes

    def __init__(self, color, flame_color):
        # these are attributes, Things objects #have or what makes up the objects
        self.model = "Tesla"
        self.color = color
        self.flame_color = flame_color
        self.is_running = False
        self.in_one_piece = True

        Car.all_cars.append(self)

    def start_car(self,):
        print("Vroom! I am on.")
        self.is_running = True

    def self_destruct(self):
        print("Boom!")
        self.in_one_piece = False

    # methods=the actions it can do(is the car on?, can #it drive?)
    @classmethod
    def all_destruct(cls):
        for car in cls.all_cars:
            car.self_destruct()


# these fill those paramentes, #they're arguments
katelyns_car = Car('white', 'gold')
tylers_car = Car('black', 'black')

katelyns_car.start_car()

print(Car.all_cars)

Car.all_destruct()

# print(katelyns_car.is_running)
# print(tylers_car.is_running)

# patricks_car = Car()
# vincent_car = Car()

# patricks_car.color = "Black"

# print(patricks_car.color)
# print(vincent_car.color)

# Car.year = 2019  # we can update the class attribute here

# patricks_car.year = 2017 #updates the class attribute individually?

# print(patricks_car.year)
