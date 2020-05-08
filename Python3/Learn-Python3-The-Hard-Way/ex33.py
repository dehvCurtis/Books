


def count_loop(): # added while loop to count_loop() func for study drill
    i = 0
    numbers = [] # creates empty list
    number_counter = input("Please type an interger >") # added for study drill
    number_counter = int(number_counter) # added for study drill

    while i < number_counter: # while i is less than 6 (added variable for study drill)
        print(f"At the top is {i}") # prints i starting at zero
        numbers.append(i) # appends i to list

        i = i + 1 # adds one to i
        print(f"Numbers now: {numbers}") # prints new list containing i + 1

        print(f"At the bottom is {i}") # prints i + 1

count_loop()


def range_loop():
    r = 0
    numbers = []

    while r in range(0,6):
        print(r)
        r = r + 1

range_loop()

# print("The numbers: ")
#
# for num in numbers: # for loop
#     print(num) # prints one number per line
