list = ['first','second','third']
dog = 'bloodhound'

# Tests for equality and inequality with strings
print(dog == 'bloodhound')
print(dog == 'lab')

# Tests using the lower() method
print(dog == dog.lower())

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
print(len(dog) < 3)

# Tests using the and keyword and the or keyword
if dog == 'bloodhound' and len(dog) < 100:
    print('success')

if dog == 'bloodhound' or len(dog) < 100:
    print('success')

# Test whether an item is in a list
print('third' in list)

# Test whether an item is not in a list
print('fourth' in list)