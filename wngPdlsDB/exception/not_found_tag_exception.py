class NotFoundTagException(Exception):
    def __init__(self, msg: str = "Can't find tag document"):
        super().__init__(msg)
