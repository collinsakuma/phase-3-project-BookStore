from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, PrimaryKeyConstraint, ForeignKey, Table

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///book_stores.db')

Base = declarative_base()

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

class Inventory(Base):
    __tablename__ = 'Inventory'
    __table_args__ = (PrimaryKeyConstraint('id'),)
    
    id = Column(Integer())
    book_id = Column(Integer(), ForeignKey('books.id'))
    store_id = Column(Integer(), ForeignKey('stores.id'))

    book = relationship('Book', backref=backref('books.id'))
    store = relationship('Store', backref=backref('stores.id'))

    def __repr__(self):
        return f"ID: {self.id}," \
            + f"Book ID: {self.book_id}," \
            + f"Store ID: {self.store_id}"

class Cart(Base):
    __tablename__ = 'Cart'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    book_id = Column(Integer())
    title = Column(String())
    price = Column(Float())

    def __repr__(self):
        return f"ID: {self.id}," \
            + f"Book ID: {self.book_id}," \
            + f"Title: {self.title}," \
            + f"Price: {self.price}"

