## ⚙️ USAGE

### Connect
```python
import wngPdlsDB

wngPdlsDB.connect(db, host, username, password)
```

### Song
```python
from wngPdlsDB.repository import SongRepository, ArtistRepository, AlbumRepository

songRepository = SongRepository()
artistRepository = ArtistRepository()
albumRepository = AlbumRepository()

artist = artistRepository.find_by_genie_id("1000")
album = albumRepository.find_by_genie_id("1000")

# create song
song = songRepository.create_song("1000", "노래", artist, album)

# find by genie id
song = songRepository.find_by_genie_id("1000")

# find all
songs = songRepository.find_all()

# find by artist
songs = songRepository.find_by_artist(artist)

# find by album
songs = songRepository.find_by_album(album)

# delete by genie id
songRepository.delete_by_genie_id("1000")
```

### Playlist
```python
from wngPdlsDB.repository import PlaylistRepository

playlistRepository = PlaylistRepository()

# create playlist
playlist = playlistRepository.create_playlist("1000", "주혜인의 플리", "같이 들을래요?", 100, 20, tags, songs)

# find by genie id
playlist = playlistRepository.find_by_genie_id("1000")

# find all
playlists = playlistRepository.find_all()

# find by tag
playlist = playlistRepository.find_by_tag(tag)

# find by song
playlist = playlistRepository.find_by_song(song)

# delete by genie id
playlistRepository.delete_by_genie_id("1000")
```

### Tag
```python
from wngPdlsDB.repository import TagRepository

tagRepository = TagRepository()

# create tag
tag = tagRepository.create_tag("T1", "행복")

# find by genie id
found = tagRepository.find_by_genie_id("T1")

# find all
founds = tagRepository.find_all()

# delete by genie id
tagRepository.delete_by_genie_id("T1")
```

### Tagged Image
```python
from wngPdlsDB.repository import TaggedImageRepository

imageRepository = TaggedImageRepository()

# create tag
tag1 = tagRepository.create_tag("T1", "행복")
tag2 = tagRepository.create_tag("T2", "슬픔")

# create image
image = imageRepository.create_image("https://wngPdls.com/image/wau2j4kjdf", [tag1, tag2])

# find by genie id
found = imageRepository.find_by_id("324dfs3233289sa034") # object id (image.id)

# find all
founds = imageRepository.find_all()

# find by tag
founds = imageRepository.find_by_tag(tag1)

# delete by genie id
imageRepository.delete_by_id("324dfs3233289sa034") # object id (image.id)
```

### Album
```python
from wngPdlsDB.repository import AlbumRepository

AlbumRepository = AlbumRepository()

# create album
album = AlbumRepository.create_album("A1", "주혜인 1집")

# find by genie id
album = AlbumRepository.find_by_genie_id("A1")

# find all
albums = AlbumRepository.find_all()

# delete by genie id
AlbumRepository.delete_by_genie_id("A1")
```

### Artist
```python
from wngPdlsDB.repository import ArtistRepository

ArtistRepository = ArtistRepository()

# create album
artist = ArtistRepository.create_artist("H1", "주혜인")

# find by genie id
artist = ArtistRepository.find_by_genie_id("H1")

# find all
artists = ArtistRepository.find_all()

# delete by genie id
ArtistRepository.delete_by_genie_id("H1")
```

## 💬 How to install

```bash
pip install requirements-dev.txt
```