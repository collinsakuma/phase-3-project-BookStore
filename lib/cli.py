from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Base, Store, Book, Inventory, Cart
from helpers import create_stores_table, cli_start, session

# engine = create_engine('sqlite:///db/book_stores.db')
# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()

if __name__ == '__main__':
    session.query(Cart).delete()
    print('Welcome to our Book store CLI app!')
    cli_start()