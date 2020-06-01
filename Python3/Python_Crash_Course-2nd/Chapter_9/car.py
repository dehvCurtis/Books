

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 10

    def get_descriptive_name(self):
        print(f'Make: {self.make}')
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')

    def odometer_reading(self):
        print(f'Odometer: {self.odometer}')

    def update_odometer(self,mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
            print(f'Mileage: {mileage}')
        else:
            print('You cant roll the odometer back!')

    def increment_odometer(self,miles):
        self.odometer += miles
        print(f'Odometer Update: {self.odometer}')

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

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
        elif self.battery_size == 100:
            pass

class ElectricCar(Car):

    def __init__(self,make,model,year):
        """ Initialize attr from Parent Class """
        super().__init__(make,model,year)
        self.battery = Battery()

    def android_capable(self):
        print(f'The {self.get_descriptive_name()} is Android Capable')

    def fill_gas_tank(self):
        print('This is an electric car. No gas tank!')

# my_car = Car('Audi','A4',2015)
# my_car.get_descriptive_name()
# my_car.odometer_reading()
# my_car.update_odometer(3)
# my_car.increment_odometer(112)