
# filename = 'cats.txt'
filename = 'dogs.txt'
# filename = 'humans.txt'

def read_file():
    while True:
        try:
            with open(filename) as cat_file:
                for line in cat_file:
                    print(line.rstrip().title())
            break
        except FileNotFoundError:
            pass
    print('\nComplete!')

read_file()