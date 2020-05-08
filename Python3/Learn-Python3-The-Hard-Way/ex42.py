# animal is-a object
class animal(object):
    pass

## dog is-a animal
class dog(animal):

    def __init__(self, name):
        # ??
        self.name = name

## cat is-a animal
class cat(animal):

    def __init__(self,name):
        ## self has-a name
        self.name = name

## person is-a object
class person(object):

    def __init__(self,name):
        ## self has-a name
        self.name = name

        # person has-a pet of some kind
        self.pet = None

## employee is-a person
class employee(person):

    def __init__(self,name,salary):
        ##
        super(employee,self).__init__(name)
        ##
        self.salary = salary

## fish has-a something
class fish(object):
    pass

## salmon is-a fish
class salmon(fish):
    pass

## halibut is-afish
class halibut(fish):
    pass


## rover is-a dog
rover = dog("Rover")

## satan is-a cat
satan = cat("satan")

## mary is-a person
mary = person("mary")

## mary has-a pet
mary.pet = satan

## frank is-a employee
frank = employee("frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a fish
flipper = fish()

## crouse is-a salmon
crouse = salmon()

## harry is-a halibut
harry = halibut()