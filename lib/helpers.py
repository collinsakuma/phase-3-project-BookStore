from db.models import Base, Store, Book, Inventory, Cart
from prettytable import PrettyTable
import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/book_stores.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_stores_table(stores):
    table = PrettyTable()
    table.title = 'List of Book Stores'
    table.field_names= ['id', 'Store Name', 'Address', 'Phone #']
    for store in stores:
        table.add_row([
            store.id,
            store.store_name,
            store.address,
            store.phone
            ])

    print(table)

def create_inventory_table(store_id):
    book_list = session.query(Inventory).filter_by(store_id=store_id)
    store_inventory = [session.query(Book).get(book.book_id) for book in book_list]
    table = PrettyTable()
    table.title = 'Blank Book Store'
    table.field_names = ['id', 'title', 'author', 'genre', 'price']
    for book in store_inventory:
        table.add_row([
            book.id,
            book.title,
            book.author,
            book.genre,
            book.price
        ])
    
    print(table)

def cli_start_menu():
        print('''
            [search (a)] -- Search for book by Title
            [stores (b)] -- Browse books by Store
            [exit   (e)] -- Leave 
        ''') 


def cli_start():
    select = ''
    cli_start_menu()
    while select != 'e':
        # shopping_cart = []

        if (select == 'a'):
            search_by_book()
        if (select == 'b'):
            browse_by_stores()

        select = click.prompt('Select Prompt')
    # print([book for book in shopping_cart])

def search_by_book():
    title = click.prompt('Enter book title to search for')
    books = session.query(Book).filter_by(title=title).all()
    if not books:
        print('No results found.')

    table = PrettyTable()
    table.title = f'Results for "{title}"'
    table.field_names = ['id', 'title', 'author', 'genre', 'price']
    for book in books:
        table.add_row([
            book.id,
            book.title,
            book.author,
            book.genre,
            book.price
        ])

    print(table)

def browse_by_stores():
    stores = session.query(Store)
    create_stores_table(stores) 

    select = click.prompt('Choose store to browse or \'e\' to leave')

    if select in ['1','2','3','4','5','6','7','8','9','10']:
        create_inventory_table(select)
            
        # while select != 'e':
        select = click.prompt('Pick a book to purchase')
        if int(select) in range(1,100):
            book_to_purchase = session.query(Book).filter(Book.id == select).all()
            print(book_to_purchase)
            added_book = Cart(
                book_id = book_to_purchase[0].id,
                title = book_to_purchase[0].title,
                price = book_to_purchase[0].price
            )
            session.add(added_book)
            session.commit()
            cli_start_menu()


def check_out_message():
    print('total is....')