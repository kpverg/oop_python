class Song:

    """
    class to represent a song
        Attributes:
            title(str):The title of the song
            artist(Artist): An Artist object representing the song creator
            duration (int): The duration of the song in seconds.May be Zero
    """

    def __init(self,title,artist,duration=0):
        """
    Song init methd 

    Args:
            title(str):initialises the 'title' attribute
            artist(Artist): At Artist object representing the song;s creator
            duration(optional[int]):initial value for the duration attribute (dafault to zero if not specified)
        """
        self.clstitle=title
        self.clsartist=artist
        self.clsduration=duration

#help(Song)
#help(Song.__init__)
#print(Song.__doc__) ###attributes class
#print(Song.__init__.__doc__)

class Album:
    """
        class to represent an album,using it;s track List

    Attributes:
        Name(str): The name of the album
        year(int):The year the album was released
        artist(Artist):The Artist responsible for the album
        default artist="Various Artists"
        tracks(List [song]):A list of the song on the album
    methods:
    addSong: Used to add a new song to the album
    """
    def __init__(self,name,year,artist=None):
        self.clsAlbName=name
        self.clsAlbYear=year
        if artist is None:
            self.clsAlbArtist=Artist("Various Artists")
        else:
            self.clsAlbArtist=artist
        self.clsAlbTracks=[]

    def addSong(self,song,position):
        """Adds a song to the track List

        Args:
            song (Song):A song to add
            position(optional[int]): if specified , the song will be added to the position
                in the track list-inserting it between other songs if necessary
                otherwise,the song will be added to the end of the list
        """
        if position is None:
            self.clsAlbTracks.append(song)
        else:
            self.clsAlbTracks.insert(position,song)

class Artist:
    """
    Basic class to store artist details.

    Attributes:
    name(str): The name of the artist
    albums(List[Album]): A list of the albums by this artist.
        the list includes only those albums in this collection, it is not an axaustive list of the artist published albums
   
    methods:
    add_album:Use to add a new album to the artist albums List    
    """
    def __init(self,name):
        self.clsArtName=name
        self.clsArtAlbums=[]

    def addAlbum(self,album):
        """Add a new album to the list

        Args:
            album(Album):Album object to add to the list
                if the album is already present, it will not added again
        """
        self.clsArtAlbums.append(album)



def load_data():
    new_artist=None
    new_album=None
    artist_list=[]

    with open("albums.txt","r") as albums:
        for line in albums:
            artist_field,album_field,year_field,song_field=tuple(line.strip("\n").split("\t"))
            year_field=int(year_field)
            print(artist_field,album_field,year_field,song_field)



if __name__=="__main__":
    load_data()