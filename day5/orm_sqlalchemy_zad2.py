# programowanie deklaratywne
# sqlalchemy 2.0

from sqlalchemy import create_engine, Integer, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int | None] = mapped_column(Integer, nullable=True)


engine = create_engine("sqlite:///osoba.db", echo=False)
Base.metadata.create_all(engine)

with Session(engine) as session:
    new_user = User(name="Ala", age=25)
    session.add(new_user)
    session.commit()

with Session(engine) as session:
    users = session.query(User).all()
    for u in users:
        print(u.id, u.name, u.age)

# 1 Ala 25
# 2 Ala 25
# nowsze podejscie
with Session(engine) as session:
    stmt = select(User)
    users = session.scalars(stmt).all()
    for u in users:
        print(u.id, u.name, u.age)
# 1 Ala 25
# 2 Ala 25
# 3 Ala 25
