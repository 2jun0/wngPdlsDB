import wngPdlsDB
import unittest
from tests.repository.common import connect_to_db
from wngPdlsDB.repository import UntaggedImageRepository
from wngPdlsDB.exception import NotFoundImageException


class TestUntaggedImage(unittest.TestCase):
    untaggedImageRepository = UntaggedImageRepository()

    @classmethod
    def setUp(cls):
        connect_to_db()

    @classmethod
    def tearDown(cls):
        wngPdlsDB.disconnect()

    def test_create_image(self):
        self.__untagged_image("http://google.com/1")

        # not exists url
        fake_url = "http://wngPdlsxltucm.com/1"
        
        self.assertRaises(
            NotFoundTagException, lambda: self.__untagged_image(fake_url)
        )

    def test_delete_by_id(self):
        # success
        image = self.__untagged_image("http://google.com/1")

        self.untaggedImageRepository.delete_by_id(image.id)
        found = self.untaggedImageRepository.find_by_id(image.id)

        assert found is None

        # not exists image
        self.assertRaises(
            NotFoundImageException, lambda: self.untaggedImageRepository.delete_by_id(image.id)
        )

    def test_find_by_id(self):
        image1 = self.__untagged_image("http://google.com/1")
        image2 = self.__untagged_image("http://google.com/2")

        found = self.untaggedImageRepository.find_by_id(image1.id)
        assert image1 == found
        assert image2 != found

    def test_find_all(self):
        image1 = self.__untagged_image("http://google.com/1")
        image2 = self.__untagged_image("http://google.com/2")

        found = self.untaggedImageRepository.find_all()
        assert image1 in found
        assert image2 in found

    def __untagged_image(self, url):
        return self.untaggedImageRepository.create_image(url)
