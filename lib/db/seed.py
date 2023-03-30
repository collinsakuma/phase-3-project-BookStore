import random 

from faker import Faker 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Store, Book, Inventory, Cart

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
    session.query(Inventory).delete()
    session.query(Cart).delete()

    book1 = Book(title="The Catcher in the Rye", author="J.D. Salinger", genre="Young adult",price=8.93)
    book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", genre="Young adult", price=8.99)
    book3 = Book(title="The Thursday Murder Club", author="Richard Osman", genre="Mystery", price=10.44)
    book4 = Book(title="The Girl with the Dragon Tattoo", author="Stieg Larsson", genre="Thriller", price=9.49)
    book5 = Book(title="The Hobbit", author="J.R.R. Tolkien", genre="Fantasy", price=15.49)
    book6 = Book(title="A Game of Thrones", author="George R.R. Martin", genre="Fantasy", price=15.49)
    book7 = Book(title="Dune", author="Frank Herbert", genre="Science fiction", price=14.99)
    book8 = Book(title="The Shining", author="Stephen King", genre="Horror", price=15.00)
    book9 = Book(title="Pet Sematary", author="Stephen King", genre="Horror", price=14.99)
    book10 = Book(title="It", author="Stephen King", genre="Horror", price=19.79)
    book11 = Book(title="Leviathan Wakes", author="James S.A. Corey", genre="Science fiction", price=14.99)
    book12 = Book(title="The Last Wish", author="Andrzej Sapowski", genre="Fantasy", price=8.99)
    book13 = Book(title="A Random Walk Down Wall Street", author="Burton G. Malkiel", genre="Non-fiction", price=26.99)
    book14 = Book(title="Liar's Poker", author="Michael Lewis", genre="Biography", price=9.99)
    book15 = Book(title="The Intellegent Investor", author="Benjamin Graham", genre="Biography", price=17.98)
    book16 = Book(title="The Great Gatsby", author="F Scott Fitzgerald", genre="Young adult", price=5.25)
    book17 = Book(title="Animal Farm", author="George Orwell", genre="fiction", price=7.48)
    session.add_all([book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,book11,book12,book13,book14,book15,book16,book17])
    session.commit()

    book_stores = []
    for store in book_store_names:
        b_store = Store(
            store_name = store,
            address = fake.address(),
            phone = f"({random.randint(100,999)})-{random.randint(100,999)}-{random.randint(1000,9999)}"
        )
        
        session.add(b_store)
        session.commit()
        book_stores.append(b_store)

    all_books = []
    all_books.extend([book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,book11,book12,book13,book14,book15,book16,book17])
    for _ in range (100):
        book = Book(
            title = fake.word(),
            author = f"{fake.first_name()} {fake.last_name()} ",
            genre = random.choice(book_genres),
            price = "%.2f" % random.uniform(9.50, 25.00)
        )
        
        session.add(book)
        session.commit()
        all_books.append(book)

    book_inventory = []
    for store in book_stores:
        for _ in range(random.randint(10,15)):
            item = Inventory(
                book_id = random.choice(all_books).id,
                store_id = store.id
            )

            session.add(item)
            session.commit()
            book_inventory.append(item)


