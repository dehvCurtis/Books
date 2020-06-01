from car import Car, ElectricCar

my_beetle = ElectricCar('VW','Jetta',2019)
my_beetle.get_descriptive_name()
my_beetle.battery.describe_battery()
my_beetle.battery.get_range()

my_tesla = ElectricCar('Tesla','Cyber Truck',2020)
my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()