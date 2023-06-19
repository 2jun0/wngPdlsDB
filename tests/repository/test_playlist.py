import dotenv
import wngPdlsDB
import os
import unittest
import mongomock
from wngPdlsDB.repository import PlaylistRepository, TagRepository


class TestPlaylist(unittest.TestCase):
    tagRepository = TagRepository()
    playlistRepository = PlaylistRepository()

    @classmethod
    def setUp(cls):
        dotenv.load_dotenv()
        host = os.environ.get("DB_HOST")
        db = os.environ.get("DB_NAME")
        username = os.environ.get("DB_USERNAME")
        password = os.environ.get("DB_PASSWORD")

        wngPdlsDB.connect(
            db=db,
            host=host,
            username=username,
            password=password,
            mongo_client_class=mongomock.MongoClient,
        )

    @classmethod
    def tearDown(cls):
        wngPdlsDB.disconnect()

    def test_create_playlist(self):
        self.__playlist(1, [self.__tag("G1", "기쁨")])

    def test_find_by_geine_id(self):
        playlist = self.__playlist(1, [self.__tag("G1", "기쁨")])

        found = self.playlistRepository.find_by_genie_id(playlist.genie_id)
        assert playlist == found

    def test_find_all(self):
        tag = self.__tag("G1", "기쁨")
        playlists = [
            self.__playlist(1, [tag]),
            self.__playlist(2, [tag]),
            self.__playlist(3, [tag]),
        ]

        found = self.playlistRepository.find_all()
        for playlist in playlists:
            assert playlist in found

    def test_find_by_tag(self):
        tag1 = self.__tag("G1", "기쁨")
        tag2 = self.__tag("G2", "슬픔")
        tag3 = self.__tag("G3", "행복")
        playlists1 = [self.__playlist(1, [tag1]), self.__playlist(2, [tag1, tag2])]
        playlists2 = [self.__playlist(3, [tag2, tag3])]

        found = self.playlistRepository.find_by_tag(tag1)
        for playlist in playlists1:
            assert playlist in found
        for playlist in playlists2:
            assert playlist not in found

    def __tag(self, genie_id, title):
        return self.tagRepository.create_tag(genie_id, title)

    def __playlist(self, genie_id, tags):
        return self.playlistRepository.create_playlist(
            genie_id, "주혜인의 플리", "스타가 될거야!", 10, 20, tags
        )
