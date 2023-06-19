import wngPdlsDB
import unittest
from tests.repository.common import connect_to_db
from wngPdlsDB.repository import TagRepository
from wngPdlsDB.exception import NotFoundTagException


class TestTag(unittest.TestCase):
    tagRepository = TagRepository()

    @classmethod
    def setUp(cls):
        connect_to_db()

    @classmethod
    def tearDown(cls):
        wngPdlsDB.disconnect()

    def test_create_tag(self):
        tag = self.__tag("G1", "기쁨")

    def test_delete_by_genie_id(self):
        tag = self.__tag("G1", "기쁨")

        self.tagRepository.delete_by_genie_id(tag.genie_id)
        found = self.tagRepository.find_by_genie_id(tag.genie_id)
        assert found is None

        # not exists playlist
        self.assertRaises(
            NotFoundTagException,
            lambda: self.tagRepository.delete_by_genie_id(tag.genie_id),
        )

    def test_find_by_geine_id(self):
        tag = self.__tag("G1", "기쁨")

        found = self.tagRepository.find_by_genie_id(tag.genie_id)
        assert tag == found

    def test_find_all(self):
        tag1 = self.__tag("G1", "기쁨")
        tag2 = self.__tag("G2", "슬픔")
        tag3 = self.__tag("G3", "행복")

        found = self.tagRepository.find_all()
        for tag in [tag1, tag2, tag3]:
            assert tag in found

    def __tag(self, genie_id, title):
        return self.tagRepository.create_tag(genie_id, title)
