# Write a generator that alternates between returning Even and Odd.

def even_odd():
    odd = 1
    even = 2
    print('Printing Odd')
    while int(odd) < 15:
        print(odd)
        odd += 1

    print('Printing Even')
    while int(even) < 15:
        print(even)
        even += 1

even_odd()