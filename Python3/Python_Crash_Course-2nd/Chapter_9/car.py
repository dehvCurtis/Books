
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


my_car = Car('Audi','A4',2015)
my_car.get_descriptive_name()
# my_car.odometer_reading()
# my_car.update_odometer(3)
# my_car.increment_odometer(112)