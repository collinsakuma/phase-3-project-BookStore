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

book_genres = ["Mystery", "Fiction", "Non-fiction", "Science fiction", "Thriller", "Horror", "Graphic novel", "Poetry", "Memoir", "Children's literature", "Biography", "Mythology", "Young adult", "Fantasy", "Fairy tale"]

if __name__ == '__main__':
    # Delete Table Data
    session.query(Store).delete()
    session.query(Book).delete()

    book_stores = []
    for store in book_store_names:
        b_store = Store(
            store_name = store,
            address = fake.address(),
            phone = fake.phone_number()
        )
        
        session.add(b_store)
        session.commit()
        book_stores.append(b_store)

    all_books = []
    for _ in range (100):
        book = Book(
            title = fake.word(),
            author = f"{fake.first_name()} {fake.last_name()} ",
            genre = random.choice(book_genres),
            price = "%.2f" % random.uniform(9.50, 40.00)
        )
        
        session.add(book)
        session.commit()
        all_books.append(book)
