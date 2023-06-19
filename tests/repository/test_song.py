import wngPdlsDB
import unittest
from tests.repository.common import connect_to_db
from wngPdlsDB.repository import (
    SongRepository,
    ArtistRepository,
    AlbumRepository,
)
from wngPdlsDB.exception import (
    NotFoundSongException,
    NotFoundArtistException,
    NotFoundAlbumException,
)
from wngPdlsDB.dto import ArtistDto, AlbumDto


class Songlist(unittest.TestCase):
    songRepository = SongRepository()
    artistRepository = ArtistRepository()
    albumRepository = AlbumRepository()

    @classmethod
    def setUp(cls):
        connect_to_db()

    @classmethod
    def tearDown(cls):
        wngPdlsDB.disconnect()

    def test_create_playlist(self):
        artist = self.__artist("H1", "주혜인")
        album = self.__album("A1", "주혜인 1집")
        self.__song("S1", "노래", artist, album)

        # not exists artist
        fake_artist = ArtistDto("123", "H3", "없는것")
        self.assertRaises(
            NotFoundArtistException, lambda: self.__song("S2", "노래", fake_artist, album)
        )

        # not exists artist
        fake_album = AlbumDto("123", "A3", "없는것")
        self.assertRaises(
            NotFoundAlbumException, lambda: self.__song("S2", "노래", artist, fake_album)
        )

    def test_delete_by_genie_id(self):
        artist = self.__artist("H1", "주혜인")
        album = self.__album("A1", "주혜인 1집")
        song = self.__song("S1", "노래", artist, album)

        self.songRepository.delete_by_genie_id(song.genie_id)
        found = self.songRepository.find_by_genie_id(song.genie_id)
        assert found is None

        # not exists song
        self.assertRaises(
            NotFoundSongException,
            lambda: self.songRepository.delete_by_genie_id(song.genie_id),
        )

    def test_find_by_geine_id(self):
        artist = self.__artist("H1", "주혜인")
        album = self.__album("A1", "주혜인 1집")
        song = self.__song("S1", "노래", artist, album)

        found = self.songRepository.find_by_genie_id(song.genie_id)
        assert song == found

    def test_find_all(self):
        artist = self.__artist("H1", "주혜인")
        album = self.__album("A1", "주혜인 1집")
        songs = [
            self.__song("S1", "노래", artist, album),
            self.__song("S2", "노래", artist, album),
            self.__song("S3", "노래", artist, album),
        ]

        found = self.songRepository.find_all()
        for song in songs:
            assert song in found

    def test_find_by_artist(self):
        artist1 = self.__artist("H1", "주혜인")
        artist2 = self.__artist("H2", "서민석")
        album1 = self.__album("A1", "주혜인 1집")
        album2 = self.__album("A2", "서민석 1집")
        album3 = self.__album("A3", "주혜인 2집")
        songs1 = [
            self.__song("S1", "노래", artist1, album1),
            self.__song("S2", "노래", artist1, album3),
        ]
        songs2 = [self.__song("S3", "노래", artist2, album2)]

        found = self.songRepository.find_by_artist(artist1)
        for song in songs1:
            assert song in found
        for song in songs2:
            assert song not in found

        # not exists artist
        fake_artist = ArtistDto("123", "H4", "없는것")

        self.assertRaises(
            NotFoundArtistException,
            lambda: self.songRepository.find_by_artist(fake_artist),
        )

    def test_find_by_album(self):
        artist1 = self.__artist("H1", "주혜인")
        artist2 = self.__artist("H2", "서민석")
        artist3 = self.__artist("H3", "이준영")
        album1 = self.__album("A1", "주혜인 1집")
        album2 = self.__album("A2", "서민석 1집")
        songs1 = [
            self.__song("S1", "노래", artist1, album1),
            self.__song("S2", "노래", artist3, album1),
        ]
        songs2 = [self.__song("S3", "노래", artist2, album2)]

        found = self.songRepository.find_by_album(album1)
        for song in songs1:
            assert song in found
        for song in songs2:
            assert song not in found

        # not exists album
        fake_album = AlbumDto("123", "A4", "없는것")

        self.assertRaises(
            NotFoundAlbumException,
            lambda: self.songRepository.find_by_album(fake_album),
        )

    def __song(self, genie_id, title, artist, album):
        return self.songRepository.create_song(genie_id, title, artist, album)

    def __artist(self, genie_id, title):
        return self.artistRepository.create_artist(genie_id, title)

    def __album(self, genie_id, title):
        return self.albumRepository.create_album(genie_id, title)
