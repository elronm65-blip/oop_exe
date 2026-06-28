class Playlist:
    def __init__(self ,name , songs =None):
        self.name = name
        if songs is None:
            songs  = []
        self.songs = songs



    def __str__(self):
       n = f"{self.name} \n"
       s = ""
       for i, sing in  enumerate(self.songs):
           s += f"{i+1}. {sing} \n"
       return  n + s

    def __repr__(self ):
        return   f"Playlist({self.name} ,{len(self.songs)} songs)"


    def __getitem__(self, index):
        return  self.songs[index]


    def __setitem__(self, index, songs):
        if self.songs[index]:
            self.songs[index] = songs

    def __len__(self):
        return len(self.songs)

    def __eq__(self ,other):
        if self.songs == other.songs and self.name == other.name:
            return True
        return False

    def __add__(self, other):
        new_name = self.name + " & " + other.name
        new_songs = self.songs + other.songs
        new_playlist = Playlist(new_name, new_songs)
        return    new_playlist

    def __contains__(self, songs):
        return songs in self.songs


    def __iter__(self):
        return iter(self.songs)

    def __bool__(self):
        if len(self.songs) > 0 or len(self.name)>0:
            return  True
        return False

    def __iadd__(self, song_or_playlist):
        if isinstance(song_or_playlist, str):
            self._songs.append(song_or_playlist)
        elif isinstance(song_or_playlist, type(self)):
            self._songs.extend(song_or_playlist._songs)
        else:
            print("שגיאה: סוג קלט לא נתמך")
        return self

    def __delitem__(self, index):
        if 0 <= index < len(self._songs) or -len(self._songs) <= index < 0:
            del self._songs[index]
        else:
            print("שגיאה: אינדקס מחוץ לטווח")

    def add_song(self, song):
        self._songs.append(song)

    def remove_song(self, song):
        if song in self._songs:
            self._songs.remove(song)
        else:
            print("שגיאה: השיר לא קיים בפלייליסט")

    def shuffle(self):
        import random
        random.shuffle(self.songs)


p1 = Playlist("moshe", ["mm","gg","hh"])
p2 = Playlist("1", [])

p3 = p1 + p2


print(p1)
p3.shuffle()

print(p3)













