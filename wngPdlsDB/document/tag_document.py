from mongoengine import Document, StringField
class TagDocument(Document):
    genie_id = StringField(required=True, unique=True)
    title = StringField(required=True, unique=True)
