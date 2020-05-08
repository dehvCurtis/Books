ten_things = "Apples Oranges Crows Phones Light Sugar"

print("Wait there aren\'t ten things in that list.")

stuff = ten_things.split(' ')
more_stuff = ["Night","Day","Entry","Test"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print(f"Adding {next_one}")
    stuff.append(next_one)
    print(f'There are {len(stuff)} items now')

print(f"There we go: {stuff}")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))