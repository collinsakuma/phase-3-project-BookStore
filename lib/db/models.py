from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///book_stores.db')

Base = declarative_base()