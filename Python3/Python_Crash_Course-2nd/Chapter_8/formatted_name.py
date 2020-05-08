# Returning a Simple Value
#
# def get_formatted_name(first_name, last_name):
#     """ Return formatted 'name' """
#     full_name = f'{first_name.title()} {last_name.title()}'
#     return full_name
#
# musician = get_formatted_name('Marilyn','Manson')
# print(musician)

# Making an Argument Optional
#
def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = f'{first_name.title()} {middle_name.title()} {last_name.title()}'
    else:
        full_name = f'{first_name.title()} {last_name.title()}'
    return full_name

shooter = get_formatted_name('Jimi','Hendricks')
print(shooter)

shooter = get_formatted_name('Harvey','lee','Oswald')
print(shooter)