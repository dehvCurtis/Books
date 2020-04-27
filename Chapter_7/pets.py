list = ['cat','dog','bird','cat','elephant','mouse','cat','fish']
print(f'List: {list}')

while 'cat' in list:
    list.remove('cat')

print(f'List: {list}')
