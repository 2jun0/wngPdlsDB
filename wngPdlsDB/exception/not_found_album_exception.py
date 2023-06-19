class NotFoundAlbumException(Exception):
    def __init__(self, msg: str = "Can't find album document"):
        super().__init__(msg)
