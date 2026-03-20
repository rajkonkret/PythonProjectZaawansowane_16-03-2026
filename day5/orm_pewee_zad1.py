from peewee import *

db = SqliteDatabase("app.db")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    age = IntegerField()


db.connect()
db.create_tables([User])

User.create(name="Jan", age=30)
User.create(name="Anna", age=22)

for user in User.select():
    print(user.name, user.age)
# Jan 30
# Anna 22