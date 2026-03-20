import logging
from peewee import *

# dodanie logowania
logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

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
# ('CREATE TABLE IF NOT EXISTS "user" ("id" INTEGER NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL,
# "age" INTEGER NOT NULL)', [])
# ('INSERT INTO "user" ("name", "age") VALUES (?, ?)', ['Jan', 30])
# ('INSERT INTO "user" ("name", "age") VALUES (?, ?)', ['Anna', 22])
# ('SELECT "t1"."id", "t1"."name", "t1"."age" FROM "user" AS "t1"', [])

print("age > 20")
# ('SELECT "t1"."id", "t1"."name", "t1"."age" FROM "user" AS "t1" WHERE ("t1"."age" > ?)', [20])
users = User.select().where(User.age > 20)
for u in users:
    print(u.name, u.age)
# age > 20
# Jan 30
# Anna 22
