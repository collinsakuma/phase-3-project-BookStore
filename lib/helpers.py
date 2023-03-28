from db.models import Base, Store, Book, Inventory
from prettytable import PrettyTable

def create_stores_table(stores):
    table  = PrettyTable()
    table.field_names= ['id', 'Store Name', 'Address', 'Phone #']
    for store in stores:
        table.add_row([
            store.id,
            store.store_name,
            store.address,
            store.phone
            ])

    print(table)
