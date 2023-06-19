import mongoengine


def connect(db: str, host: str, username: str, password: str):
    mongoengine.connect(db, host=host, username=username, password=password)