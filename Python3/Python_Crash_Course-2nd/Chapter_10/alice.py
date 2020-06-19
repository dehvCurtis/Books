
filename = 'alice.txt'
# title = 'Alice in Wonderland'

try:
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
except FileNotFoundError:
    print('File not found!')
else:
    words = contents.split()
    num_words = len(words)
    print(f'The file {filename} has appx {num_words} number of words')