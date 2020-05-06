
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

# print(make_album('Various Artists','Xmas Music'))
print(make_album('Various Artists','Xmas Music',"9"))