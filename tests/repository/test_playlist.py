import wngPdlsDB
import unittest
from tests.repository.common import connect_to_db
from wngPdlsDB.repository import (
    PlaylistRepository,
    TagRepository,
    SongRepository,
    ArtistRepository,
    AlbumRepository,
)
from wngPdlsDB.exception import (
    NotFoundPlaylistException,
    NotFoundTagException,
    NotFoundSongException,
)
from wngPdlsDB.dto import TagDto, SongDto


class TestPlaylist(unittest.TestCase):
    tagRepository = TagRepository()
    songRepository = SongRepository()
    playlistRepository = PlaylistRepository()
    artistRepository = ArtistRepository()
    albumRepository = AlbumRepository()

    @classmethod
    def setUp(cls):
        connect_to_db()

    @classmethod
    def tearDown(cls):
        wngPdlsDB.disconnect()

    def test_create_playlist(self):
        tag = self.__tag("G1", "기쁨")
        album = self.__album("A1", "주혜인 1집")
        artist = self.__artist("H1", "주혜인")
        song = self.__song("S1", "노래", artist, album)
        self.__playlist("2", [tag], [song])

        # not exists tag
        fake_tag = TagDto("123", "G3", "없는것")
        self.assertRaises(
            NotFoundTagException, lambda: self.__playlist("3", [fake_tag])
        )

        # not exists song
        fake_song = SongDto("1234", "S3", "없는것", artist, album)
        self.assertRaises(
            NotFoundSongException, lambda: self.__playlist("3", [tag], [fake_song])
        )

    def test_delete_by_genie_id(self):
        tag = self.__tag("G1", "기쁨")
        playlist = self.__playlist("1", [tag])

        self.playlistRepository.delete_by_genie_id(playlist.genie_id)
        found = self.playlistRepository.find_by_genie_id(playlist.genie_id)
        assert found is None

        # not exists playlist
        self.assertRaises(
            NotFoundPlaylistException,
            lambda: self.playlistRepository.delete_by_genie_id(playlist.genie_id),
        )

    def test_find_by_geine_id(self):
        playlist = self.__playlist("1", [self.__tag("G1", "기쁨")])

        found = self.playlistRepository.find_by_genie_id(playlist.genie_id)
        assert playlist == found

    def test_find_all(self):
        tag = self.__tag("G1", "기쁨")
        playlists = [
            self.__playlist("1", [tag]),
            self.__playlist("2", [tag]),
            self.__playlist("3", [tag]),
        ]

        found = self.playlistRepository.find_all()
        for playlist in playlists:
            assert playlist in found

    def test_find_by_tag(self):
        tag1 = self.__tag("G1", "기쁨")
        tag2 = self.__tag("G2", "슬픔")
        tag3 = self.__tag("G3", "행복")
        playlists1 = [self.__playlist("1", [tag1]), self.__playlist("2", [tag1, tag2])]
        playlists2 = [self.__playlist("3", [tag2, tag3])]

        found = self.playlistRepository.find_by_tag(tag1)
        for playlist in playlists1:
            assert playlist in found
        for playlist in playlists2:
            assert playlist not in found

        # not exists tag
        fake_tag = TagDto("123", "G4", "없는것")

        self.assertRaises(
            NotFoundTagException, lambda: self.playlistRepository.find_by_tag(fake_tag)
        )

    def test_find_by_tag(self):
        tag1 = self.__tag("G1", "기쁨")
        tag2 = self.__tag("G2", "슬픔")
        tag3 = self.__tag("G3", "행복")
        playlists1 = [self.__playlist("1", [tag1]), self.__playlist("2", [tag1, tag2])]
        playlists2 = [self.__playlist("3", [tag2, tag3])]

        found = self.playlistRepository.find_by_tag(tag1)
        for playlist in playlists1:
            assert playlist in found
        for playlist in playlists2:
            assert playlist not in found

        # not exists tag
        fake_tag = TagDto("123", "G4", "없는것")

        self.assertRaises(
            NotFoundTagException, lambda: self.playlistRepository.find_by_tag(fake_tag)
        )

    def test_find_by_song(self):
        tag = self.__tag("G1", "기쁨")
        album = self.__album("A1", "주혜인 1집")
        artist = self.__artist("H1", "주혜인")

        song1 = self.__song("S1", "노래", artist, album)
        song2 = self.__song("S2", "노래", artist, album)
        song3 = self.__song("S3", "노래", artist, album)
        playlists1 = [
            self.__playlist("1", [tag], [song1]),
            self.__playlist("2", [tag], [song1, song2]),
        ]
        playlists2 = [self.__playlist("3", [tag], [song2, song3])]

        found = self.playlistRepository.find_by_song(song1)
        for playlist in playlists1:
            assert playlist in found
        for playlist in playlists2:
            assert playlist not in found

        # not exists song
        fake_song = SongDto("1234", "S4", "노래", artist, album)

        self.assertRaises(
            NotFoundSongException,
            lambda: self.playlistRepository.find_by_song(fake_song),
        )

    def __tag(self, genie_id, title):
        return self.tagRepository.create_tag(genie_id, title)

    def __song(self, genie_id, title, artist, album):
        return self.songRepository.create_song(genie_id, title, artist, album)

    def __artist(self, geine_id, title):
        return self.artistRepository.create_artist("123", "주혜인")

    def __album(self, genie_id, title):
        return self.albumRepository.create_album("1234", "주혜인 1집")

    def __playlist(self, genie_id, tags, songs=[]):
        return self.playlistRepository.create_playlist(
            genie_id, "주혜인의 플리", "스타가 될거야!", 10, 20, tags, songs
        )
