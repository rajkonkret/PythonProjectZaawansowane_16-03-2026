from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# podstawowa klasa
Base = declarative_base()


# definicja modelu - odwzorowanie tabeli, (encja)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)


# silnik
engine = create_engine('sqlite:///osoba.db', echo=True)  # echo=True - logowanie zdarzen z bazy danych

# tworzenie tabel w bazie danych
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# nowy użytkownik
# 2026-03-20 12:33:29,181 INFO sqlalchemy.engine.Engine INSERT INTO users (name, age) VALUES (?, ?)
new_user = User(name="Ala", age=25)
session.add(new_user)
session.commit()

# 2026-03-20 12:33:29,192 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name,
# users.age AS users_age
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)
session.close()
