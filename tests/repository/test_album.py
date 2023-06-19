import wngPdlsDB
import unittest
from tests.repository.common import connect_to_db
from wngPdlsDB.repository import AlbumRepository
from wngPdlsDB.exception import NotFoundAlbumException


class TestAlbum(unittest.TestCase):
    albumRepository = AlbumRepository()

    @classmethod
    def setUp(cls):
        connect_to_db()

    @classmethod
    def tearDown(cls):
        wngPdlsDB.disconnect()

    def test_create_album(self):
        album = self.__album("A1", "주혜인 1집")

    def test_delete_by_genie_id(self):
        album = self.__album("A1", "주혜인 1집")

        self.albumRepository.delete_by_genie_id(album.genie_id)
        found = self.albumRepository.find_by_genie_id(album.genie_id)
        assert found is None

        # not exists playlist
        self.assertRaises(
            NotFoundAlbumException,
            lambda: self.albumRepository.delete_by_genie_id(album.genie_id),
        )

    def test_find_by_geine_id(self):
        album = self.__album("A1", "주혜인 1집")

        found = self.albumRepository.find_by_genie_id(album.genie_id)
        assert album == found

    def test_find_all(self):
        album1 = self.__album("A1", "주혜인 1집")
        album2 = self.__album("A2", "주혜인 2집")
        album3 = self.__album("A3", "주혜인 3집")

        found = self.albumRepository.find_all()
        for album in [album1, album2, album3]:
            assert album in found

    def __album(self, genie_id, title):
        return self.albumRepository.create_album(genie_id, title)
