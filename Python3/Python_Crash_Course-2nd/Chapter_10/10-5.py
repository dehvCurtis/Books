
with open('/tmp/test.txt', 'w') as file:
    while True:
        language = input('What is your favorite programming language?')
        if language != 'quit':
            file.write(f'\t- {language}\n')
        elif language == 'quit':
            print('quitting')
            break
