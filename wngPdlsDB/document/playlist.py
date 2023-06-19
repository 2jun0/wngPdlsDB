from mongoengine import Document, StringField, IntField, DateTimeField

class Playlist(Document):
    genie_id = IntField(required=True)
    title = StringField(required=True)
    description = StringField(required=True)
    likes = IntField(required=True)
    views = IntField(required=True)
    created_date = DateTimeField(required=True)
    updated_date = DateTimeField(required=True)