import wngPdlsDB
import unittest
from tests.repository.common import connect_to_db
from wngPdlsDB.repository import TaggedImageRepository, TagRepository
from wngPdlsDB.dto import TagDto
from wngPdlsDB.exception import NotFoundTagException, NotFoundImageException


class TestImage(unittest.TestCase):
    tagRepository = TagRepository()
    imageRepository = TaggedImageRepository()

    @classmethod
    def setUp(cls):
        connect_to_db()

    @classmethod
    def tearDown(cls):
        wngPdlsDB.disconnect()

    def test_create_image(self):
        tag = self.__tag("G1", "기쁨")
        self.__image("http://google.com/1", tag)

        # not exists tag
        fake_tag = TagDto("123", "G3", "없는것")
        self.assertRaises(
            NotFoundTagException, lambda: self.__image("http://google.com/2", fake_tag)
        )

    def test_delete_by_id(self):
        # success
        tag = self.__tag("G1", "기쁨")
        image = self.__image("http://google.com/1", tag)

        self.imageRepository.delete_by_id(image.id)
        found = self.imageRepository.find_by_id(image.id)

        assert found is None

        # not exists image
        self.assertRaises(
            NotFoundImageException, lambda: self.imageRepository.delete_by_id(image.id)
        )

    def test_find_by_id(self):
        tag = self.__tag("G1", "기쁨")
        image1 = self.__image("http://google.com/1", tag)
        image2 = self.__image("http://google.com/2", tag)

        found = self.imageRepository.find_by_id(image1.id)
        assert image1 == found
        assert image2 != found

    def test_find_all(self):
        tag = self.__tag("G1", "기쁨")
        image1 = self.__image("http://google.com/1", tag)
        image2 = self.__image("http://google.com/2", tag)

        found = self.imageRepository.find_all()
        assert image1 in found
        assert image2 in found

    def test_find_by_tag(self):
        # success
        tag1 = self.__tag("G1", "기쁨")
        tag2 = self.__tag("G2", "슬픔")
        images1 = [
            self.__image("http://google.com/1", tag1),
            self.__image("http://google.com/2", tag1),
        ]
        images2 = [self.__image("http://google.com/3", tag2)]

        found = self.imageRepository.find_by_tag(tag1)
        for image in images1:
            assert image in found
        for image in images2:
            assert image not in found

        # not exists tag
        fake_tag = TagDto("123", "G3", "없는것")

        self.assertRaises(
            NotFoundTagException, lambda: self.imageRepository.find_by_tag(fake_tag)
        )

    def __tag(self, genie_id, title):
        return self.tagRepository.create_tag(genie_id, title)

    def __image(self, url, tag):
        return self.imageRepository.create_image(url, tag)
