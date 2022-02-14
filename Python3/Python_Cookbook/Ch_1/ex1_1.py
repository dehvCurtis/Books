p = (4,5)
x, y = p
print(f'Printing x: {x}')
print(f'Printing y: {y}')

data = ['ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print(name)
print(shares)
print(date)

name, shares, price, (year, month, day) = data
print(month)
