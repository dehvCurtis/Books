
class Car:
    """ A simple car class """

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f'Odometer: {self.odometer}')

    def update_odometer(self,mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print('You cannot roll it back')

    def increment_odometer(self,miles):
        self.odometer += miles

class Battery:

    def __init__(self,battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'Battery Size: {self.battery_size}kWh')

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f'This car can go {range} on a full battery')

class ElectricCar(Car):

    def __init__(self,make,model,year):
        """ Initialize attr from Parent Class """
        super().__init__(make,model,year)
        self.battery = Battery()

    def android_capable(self):
        print(f'The {self.get_descriptive_name()} is Android Capable')

    def fill_gas_tank(self):
        print('This is an electric car. No gas tank!')


# tesla = ElectricCar("tesla","Model 3",2018)
# print(tesla.get_descriptive_name())

# tesla.describe_battery()
# tesla.android_capable()
# tesla.fill_gas_tank()
# tesla.battery.describe_battery()
# tesla.battery.get_range()