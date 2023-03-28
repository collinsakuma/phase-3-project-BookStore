from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Store, Book

if __name__ == '__main__':

    engine = create_engine('sqlite:///book_stores.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()