# Adding New Key-Value Pairs
# alien_0 = {'color':'green', 'points':'5'}
#
# print(alien_0)
#
# alien_0['x-position'] = 0
# alien_0['y-position'] = 25
# print(alien_0)

# Starting with an Empty Dictionary
# alien_0 = {}
#
# alien_0['color'] = 'red'
# alien_0['points'] = '5'
#
# print(alien_0)

# Modifying Values in a Dictionary
# alien_0 = {'color':'green'}
# print(f'The color of the alien: {alien_0["color"]}')
#
# alien_0['color'] = 'yellow'
# print(f'The color is now: {alien_0["color"]}')
#
# alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f'Original Position: {alien["x_position"]}')
#
# print(f'Updating speed to fast')
# alien['speed'] = 'fast'
#
# if alien['speed'] == 'slow':
#     x_increment = 1
# elif alien['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien['x_position'] = alien['x_position'] + x_increment
#
# print(f'New Position: {alien["x_position"]}')

# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['color']
print(alien_0)