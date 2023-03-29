from db.models import Base, Store, Book, Inventory
from prettytable import PrettyTable
import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/book_stores.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_stores_table(stores):
    table  = PrettyTable()
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
    end_list = [session.query(Book).get(book.book_id) for book in book_list]
    table = PrettyTable()
    table.title = 'Blank Book Store'
    table.field_names = ['id', 'title', 'author', 'genre', 'price']
    for book in end_list:
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

        if (select == 'a'):
            search_by_book()
        if (select == 'b'):
            browse_by_stores()

        select = click.prompt('Select Prompt')

def search_by_book():
    pass

def browse_by_stores():
    select = ''
    while select != 'e':
        stores = session.query(Store)
        create_stores_table(stores) 

        select = click.prompt('Choose store to browse or e to leave')
        # ewww fix this
        if (select == "1"):
            create_inventory_table('1')
        if (select == "2"):
            create_inventory_table('2')
        if (select == "3"):
            create_inventory_table('3')
        if (select == "4"):
            create_inventory_table('4')
        if (select == "5"):
            create_inventory_table('5')
        if (select == "6"):
            create_inventory_table('6')
        if (select == "6"):
            create_inventory_table('6')
        if (select == "7"):
            create_inventory_table('7')
        if (select == "8"):
            create_inventory_table('8')
        if (select == "9"):
            create_inventory_table('9')
        if (select == "10"):
            create_inventory_table('10')