places = ['Belgium','Spain','France','England','Switzerland']

#Print your list in its original order.
for p in places:
    print(p)

#Use sorted() to print your list in alphabetical order
print(sorted(places))

print(places)

# Use sorted() to print your list in reverse alphabetical order
print(sorted(places, reverse=True))

places.reverse()
print(places)

# Use sort() to change your list so it’s stored in alphabetical order.
places.sort()
print(places)

# Use sort() to change your list so it’s stored in reverse alphabetical order.
places.sort(places.reverse())