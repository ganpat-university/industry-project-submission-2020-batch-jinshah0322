class Song:
    def __init__(self, title, artist, genre):
        self.title = title
        self.artist = artist
        self.genre = genre

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

class User:
    def __init__(self, username):
        self.username = username
        self.playlists = []
        self.favorite_genres = set()

    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)

    def add_song_to_playlist(self, playlist, song):
        if playlist in self.playlists:
            playlist.add_song(song)

    def recommend_song(self, song):
        print(f"Hey {self.username}! We recommend the song '{song.title}' by {song.artist}.")

    def track_preferences(self, song):
        self.favorite_genres.add(song.genre)

user1 = User("Alice")
user2 = User("Bob")

song1 = Song("Shape of You", "Ed Sheeran", "Pop")
song2 = Song("Stairway to Heaven", "Led Zeppelin", "Rock")

user1.create_playlist("Favorites")
user1.add_song_to_playlist(user1.playlists[0], song1)
user1.add_song_to_playlist(user1.playlists[0], song2)

user1.recommend_song(song1)
user2.track_preferences(song2) 

print(f"{user2.username}'s Favorite Genres: {user2.favorite_genres}")