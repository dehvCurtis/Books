# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). This method should check the battery size and set the capacity to 100 if it isn’t already.

from electric_car import Car

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

# Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.

nissan = ElectricCar('Nissan','Altima',2019)
nissan.battery.get_range()
nissan.battery.upgrade_battery()
nissan.battery.get_range()
