# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
list = ('thai','japanese','mexican','italian')

# Use a for loop to print each food the restaurant offers.
print(f'Food being offered:')
for food in list:
    print('\t-',food)

# Try to modify one of the items, and make sure that Python rejects the change.
# list[0] = 'test'
# print(list)

# The restaurant changes its menu, replacing two of the items with different foods.
# Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
list = ('thai','japanese','mexican','italian', 'korean')
print(f'Food being offered:')
for food in list:
    print('\t-',food)