import ipdb 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Store, Book, Inventory

if __name__ == '__main__':

    engine = create_engine('sqlite:///db/book_stores.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    #get first store object
    first_store = session.query(Store).first()
    #get list of books with the store id of 1
    book_list = session.query(Inventory).filter_by(store_id=first_store.id)
    #get list of book objects
    end_list = [session.query(Book).get(book.book_id) for book in book_list]
    print([book for book in end_list])
    # prints like 
    # [ID: 95,Title: foot,Author: Michael Hernandez ,Genre: Fiction,Price: 14.09, ID: 95,Title: foot,Author: Michael Hernandez ,Genre: Fiction,Price: 14.09, .....
    
    
    #query = session.query(Sighting).filter(Sighting.id == '1').all()
    query = session.query(Store).filter(Store.id == '1').all()
    ipdb.set_trace()
