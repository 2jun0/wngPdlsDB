from mongoengine import Document, StringField, IntField, DateTimeField


class Playlist(Document):
    genie_id = IntField(required=True, unique=True)
    title = StringField(required=True)
    description = StringField(required=True)
    likes = IntField(required=True, min_value=0)
    views = IntField(required=True, min_value=0)
    created_date = DateTimeField(required=True)
    updated_date = DateTimeField(required=True)
