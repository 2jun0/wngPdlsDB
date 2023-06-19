import dotenv
import wngPdlsDB
import os
import mongomock


def connect_to_db():
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
