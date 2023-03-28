from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, PrimaryKeyConstraint, ForeignKey, Table

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///book_stores.db')

Base = declarative_base()

# store_books = Table(
#     'store_books',
#     Base.metadata,
#     Column('book_id', ForeignKey('books.id'), primary_key=True),
#     Column('store_id', ForeignKey('stores.id'), primary_key=True)
# )

class Store(Base):
    __tablename__ = 'stores'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    store_name = Column(String())
    address = Column(String())
    phone = Column(Integer())

    def __repr__(self):
        return f"ID: {self.id}," \
            + f"Store Name: {self.store_name}," \
            + f"Address: {self.address}," \
            + f"Phone: {self.phone}"


class Book(Base):
    __tablename__ = 'books'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    title = Column(String())
    author = Column(String())
    genre = Column(String())
    price = Column(Float())

    def __repr__(self):
        return f"ID: {self.id}," \
            + f"Title: {self.title}," \
            + f"Author: {self.author}," \
            + f"Genre: {self.genre}," \
            + f"Price: {self.price}"
