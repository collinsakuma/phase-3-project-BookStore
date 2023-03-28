import ipdb 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Store, Book, Inventory

if __name__ == '__main__':

    engine = create_engine('sqlite:///db/book_stores.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()