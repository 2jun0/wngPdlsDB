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

```

### Tag
```python
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