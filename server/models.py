import mongoengine as me


class Sorvete(me.EmbeddedDocument):
    s_id = me.IntField()
    name = me.StringField()
    description = me.StringField()
    price = me.FloatField()


class Sorveteria(me.Document):
    name = me.StringField()
    slogan = me.StringField()
    sorvetes = me.EmbeddedDocumentListField(Sorvete)
