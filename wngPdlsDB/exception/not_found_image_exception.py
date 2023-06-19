class NotFoundImageException(Exception):
    def __init__(self, msg: str = "Can't find image document"):
        super().__init__(msg)
