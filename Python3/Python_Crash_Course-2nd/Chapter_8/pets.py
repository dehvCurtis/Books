# Positional Arguments
# def describe_pet(animal_type, ainmal_name):
#     """ DISPLAY INFO ABOUT PET """
#     print(f'\nAnimal Type: {animal_type.title()}')
#     print(f'Animal Name: {ainmal_name.title()}')
#
# describe_pet('Dog','Dakota')
# describe_pet('Cat','Owen')

# Keyword Arguments
# def describe_pet(animal_type, ainmal_name):
#     """ DISPLAY INFO ABOUT PET """
#     print(f'\nAnimal Type: {animal_type.title()}')
#     print(f'My {animal_type}\'s name is {ainmal_name.title()}')
#
# describe_pet(animal_type='dog',ainmal_name='dakota')

# Default Values
def describe_pet(animal_name, animal_type='dog'):
    """ DISPLAY INFO ABOUT PET """
    print(f'\nAnimal Type: {animal_type.title()}')
    print(f'My {animal_type}\'s name is {animal_name.title()}')

# describe_pet('willie')
