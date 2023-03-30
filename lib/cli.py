from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Base, Store, Book, Inventory, Cart
from helpers import create_stores_table, cli_start, session, cli_end

# engine = create_engine('sqlite:///db/book_stores.db')
# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()

if __name__ == '__main__':
    session.query(Cart).delete()
    print('''
$$$$$$$\                      $$\              $$$$$$\    $$\                                   
$$  __$$\                     $$ |            $$  __$$\   $$ |                                  
$$ |  $$ | $$$$$$\   $$$$$$\  $$ |  $$\       $$ /  \__|$$$$$$\    $$$$$$\   $$$$$$\   $$$$$$\  
$$$$$$$\ |$$  __$$\ $$  __$$\ $$ | $$  |      \$$$$$$\  \_$$  _|  $$  __$$\ $$  __$$\ $$  __$$\ 
$$  __$$\ $$ /  $$ |$$ /  $$ |$$$$$$  /        \____$$\   $$ |    $$ /  $$ |$$ |  \__|$$$$$$$$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$  _$$<        $$\   $$ |  $$ |$$\ $$ |  $$ |$$ |      $$   ____|
$$$$$$$  |\$$$$$$  |\$$$$$$  |$$ | \$$\       \$$$$$$  |  \$$$$  |\$$$$$$  |$$ |      \$$$$$$$\ 
\_______/  \______/  \______/ \__|  \__|       \______/    \____/  \______/ \__|       \_______|
                                                                                                
                                                                                                
                                                                                                
Welcome to our BOOK STORE CLI app!
    ''')
    cli_start()
    cli_end()