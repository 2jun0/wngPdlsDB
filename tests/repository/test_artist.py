import wngPdlsDB
import unittest
from tests.repository.common import connect_to_db
from wngPdlsDB.repository import ArtistRepository
from wngPdlsDB.exception import NotFoundArtistException


class TestArtist(unittest.TestCase):
    artistRepository = ArtistRepository()

    @classmethod
    def setUp(cls):
        connect_to_db()

    @classmethod
    def tearDown(cls):
        wngPdlsDB.disconnect()

    def test_create_artist(self):
        artist = self.__artist("H1", "주혜인")

    def test_delete_by_genie_id(self):
        artist = self.__artist("H1", "주혜인")

        self.artistRepository.delete_by_genie_id(artist.genie_id)
        found = self.artistRepository.find_by_genie_id(artist.genie_id)
        assert found is None

        # not exists playlist
        self.assertRaises(
            NotFoundArtistException,
            lambda: self.artistRepository.delete_by_genie_id(artist.genie_id),
        )

    def test_find_by_geine_id(self):
        artist = self.__artist("H1", "주혜인")

        found = self.artistRepository.find_by_genie_id(artist.genie_id)
        assert artist == found

    def test_find_all(self):
        artist1 = self.__artist("H1", "주혜인")
        artist2 = self.__artist("H2", "서민석")
        artist3 = self.__artist("H3", "이준영")

        found = self.artistRepository.find_all()
        for artist in [artist1, artist2, artist3]:
            assert artist in found

    def __artist(self, genie_id, title):
        return self.artistRepository.create_artist(genie_id, title)
