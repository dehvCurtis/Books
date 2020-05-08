lyrics = Song(["This is a song","song about something"])

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


bday_song = Song([
    "Happy bday to you",
    "Happy bday to you...."])

bulls_on_parade = Song([
    "Bulls on parade",
    "They rally around the family"])


bday_song.sing_me_a_song()
bulls_on_parade.sing_me_a_song()