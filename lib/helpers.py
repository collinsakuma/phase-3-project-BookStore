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
    store_names = ['Book Addict','Book Bin','Hooked on Books','The Book Worm','A Likely Story'
                    ,'Books 4 Less','Open Books','Neighborhood Books','Booked','The Book Store']
    chosen_store = store_names[int(store_id)-1]
    book_list = session.query(Inventory).filter_by(store_id=store_id)
    store_inventory = [session.query(Book).get(book.book_id) for book in book_list]
    table = PrettyTable()
    table.title = f"{chosen_store}"
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
    [Title  (a)] -- Search for book by Title
    [Genre  (b)] -- Search by Genre
    [Store  (c)] -- Browse books by Store
    [exit   (e)] -- Checkout or Exit 
        ''') 


def cli_start():
    select = ''
    cli_start_menu()
    while select != 'e':
        if (select == 'a'):
            search_by_book()
        if (select == 'b'):
            search_by_genre()
        if (select == 'c'):
            browse_by_stores()

        select = click.prompt('Select Prompt')

def search_by_book():
    title = click.prompt('\nEnter book title to search for')
    books = session.query(Book).filter_by(title=title).all()
    if not books:
        print('No results found.')
        cli_start_menu()
    else:
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
        add_book_to_cart()
    
def search_by_genre():
    print('''
    Genres:
    1. Biography                6.  Graphic Novel   11. Non-fiction
    2. Children's Literature    7.  Horror          12. Poetry
    3. Fairy Tale               8.  Memoir          13. Science Fiction
    4. Fantasy                  9.  Mystery         14. Thriller
    5. Fiction                  10. Mythology       15. Young Adult
    ''')
    select = click.prompt("Choose Genre or 'e' to go back")
    try:
        if select == 'e':
            cli_start_menu()
        elif int(select) in range(1,16):
            genre_list = ['Biography','Children\'s literature','Fairy tale','Fantasy','Fiction','Graphic novel'
                        ,'Horror','Memoir','Mystery','Mythology','Non-fiction','Poetry','Science fiction'
                        ,'Thriller','Young adult']
            chosen_genre = (genre_list[int(select)-1])
            books_matching_genre = session.query(Book).filter_by(genre=chosen_genre).all()
            table = PrettyTable()
            table.title = f"{chosen_genre} Books"
            table.field_names = ['id', 'title', 'author', 'genre', 'price']
            for book in books_matching_genre:
                table.add_row([
                    book.id,
                    book.title,
                    book.author,
                    book.genre,
                    book.price
                ])
            print(table)
            add_book_to_cart()
    except ValueError:
        print('Invalid Input')
        search_by_genre()


def browse_by_stores():
    stores = session.query(Store)
    create_stores_table(stores) 

    select = click.prompt('Enter store ID to view its inventory or \'e\' to leave')
    try:
        if select == 'e':
            cli_start_menu()
        elif int(select) in range(1,11):
            create_inventory_table(select)
            add_book_to_cart()
    except ValueError:
        print('Invalid Input')
        browse_by_stores()

def add_book_to_cart():
    select = click.prompt('\nEnter Book ID to add to Cart or exit with \'e\'')
    try:
        if select =='e':
            cli_start_menu()
        elif int(select) in range(1,118):
            book_to_purchase = session.query(Book).filter(Book.id == select).all()
            print('')
            print(f"\"{book_to_purchase[0].title}\" added to Cart")
            added_book = Cart(
                book_id = book_to_purchase[0].id,
                title = book_to_purchase[0].title,
                price = book_to_purchase[0].price
            )
            session.add(added_book)
            session.commit()
            print('''
continue shopping or checkout/leave with 'e'
            ''')
            cli_start_menu()
    except ValueError:
        print('Invalid Input')
        add_book_to_cart()


def cli_end():
    books_in_cart = session.query(Cart).all()
    if len(books_in_cart) > 0:
        cart_total = 0
        for book in books_in_cart:
            cart_total += book.price
        table = PrettyTable()
        table.title = 'Books in Cart'
        table.field_names = ['Book ID', 'Title', 'Price']
        for book in books_in_cart:
            table.add_row([
                book.book_id,
                book.title,
                f"$ {book.price:.2f}"
            ])

        print(table)
        print("\n""Your total is: "+"$" + "%.2f" % cart_total)
    else:
        print('no books in cart')
    
    
    print('''
       .--.           .---.        .-.
   .---|--|   .-.     |~~~|  .---. |~|    .--.
.--|===|Od|---|_|--.__| D |--|:::| |~|-==-|==|---.
|%%|Lev|ys|===| |~~|%%| u |--|   |_|~|1984|  |___|-.
|  |iat|se|===| |==|  | n |  |:::|=| |    |It|---|=|
|  |han|y |   |_|__|  | e |__|   | | |    |  |___| |
|~~|===|--|===|~|~~|%%|~~~|--|:::|=|~|----|==|---|=|
^--^---'--^---^-^--^--^---'--^---^-^-^-==-^--^---^-'

               Thank you come again!

    ''')
    