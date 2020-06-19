# 10-4. Guest Book: Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.

filename = 'guest.txt'

def loop():
    with open(filename, 'a') as file:
        while True:
            name = input('Please enter your name or \'quit\' to exit > ')
            if name == 'quit':
                break
            else:
                print(f'Hello {name.title()}')
                file.write(name)
                loop()

loop()