word = input('Please type a word in upper or lower case.')

def which_case(word1):

    if word1 == word.upper():
        print(f'{word} is upper case')
    else:
        print(f'{word} is lower case')

which_case(word)