
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        pass
        # print(f'File {filename} not found!')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} has appx {num_words} number of words')

filenames = ['alice.txt','Pride_and_Prejudice.txt','Frankenstein.txt']

for i in filenames:
    count_words(i)