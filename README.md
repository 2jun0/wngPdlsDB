## ⚙️ USAGE

### Connect
```python
import wngPdlsDB

wngPdlsDB.connect(db, host, username, password)
```

### Song
```python

```

### Playlist
```python
from wngpdlsDB.repository import PlaylistRepository

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
from wngpdlsDB.repository import TagRepository

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

### Image
```python
from wngpdlsDB.repository import ImageRepository

imageRepository = ImageRepository()

# create image
image = imageRepository.create_image("https://wngPdls.com/image/wau2j4kjdf", tag)

# find by genie id
found = imageRepository.find_by_id("324dfs3233289sa034") # object id (image.id)

# find all
founds = imageRepository.find_all()

# find by tag
founds = imageRepository.find_by_tag(tag)

# delete by genie id
imageRepository.delete_by_id("324dfs3233289sa034") # object id (image.id)
```

### Album
```python

```

### Artist
```python

```

## 💬 How to install

```bash
pip install requirements-dev.txt
```