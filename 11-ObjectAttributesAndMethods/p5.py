class Song():

    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return f"Performer: {self.artist}\nSong: {self.title}\nAlbum: {self.album}\nYear: {self.year}"


song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", "2017")
song2 = Song("Queen", "We Will Rock You", "News of the World", "1977")
song3 = Song("Nirvana", "Smells Like Teen Spirit", "Nevermind", "1991")

print(song1)
print()
print(song2)
print()
print(song3)
