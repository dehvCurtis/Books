dict = {}
def make_album(artist,album,num_songs=None):
    dict = {'artist':artist,'album':album}
    if num_songs != None:
        dict['songs'] = num_songs
    if num_songs == None:
        formatted = f'Artist: {dict["artist"]}\nAlbum: {dict["album"]}'
    elif num_songs != None:
        formatted = f'Artist: {dict["artist"]}\nAlbum: {dict["album"]}\nSongs: {dict["songs"]}'
    # formatted = formatted.title()
    print(formatted)

# Write a while loop that allows users to enter an album’s artist and title.
while True:
    artist_name = input('Please enter Artist: ')
    if artist_name == 'quit':
        break
    dict['artist'] = artist_name

    album_name = input('Please enter Album: ')
    if album_name == 'quit':
        break
    dict['album'] = album_name

    number_songs = input('How many songs: ')
    if number_songs == 'quit':
        break
    elif number_songs == '':
        number_songs = None
    dict['num_songs'] = number_songs

    print(f'Artist: {artist_name}')
    print(f'Album: {album_name}')
    print(f'Songs: {number_songs}')



# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.