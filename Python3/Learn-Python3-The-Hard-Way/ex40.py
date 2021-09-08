class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy bday to you","Happy bday to you!"])
bulls_parade = Song(["They rally around the family","With pockets full of shells"])

happy_bday.sing_song()