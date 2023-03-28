import random 

from faker import Faker 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Store, Book

engine = create_engine('sqlite:///book_stores.db')
Session = sessionmaker(bind = engine)
session = Session()

# faker object
fake = Faker()

book_store_names = ["Book Addict", "Book Bin", "Hooked on Books", "The Book Worm", "A Likely Story", "Books 4 Less", "Open Books", "Neighborhood Books", "Booked", "The Book Store"]

if __name__ == '__main__':
    # Delete Table Data
    session.query(Store).delete()


    book_stores = []
    for store in book_store_names:
        b_store = Store(
            store_name = store,
            address = fake.address(),
            phone = random.randint(1000000000, 9999999999)
        )
        
        session.add(b_store)
        session.commit()
        book_stores.append(b_store)