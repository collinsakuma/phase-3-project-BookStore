CLI Bookstore

## Description
This is a CLI applicaiton allowing users to browse the inventory of different book store location and add books to a "shopping cart" displaying the total cost of all books selected. 

### Users can:
- Browse books available by location
- Search for books by title or genre
- Add books by id to a "cart" and show the total cost. 

Wireframing for db table construction: https://wireframe.cc/6VVkQm

## Instructions

After cloning repository to your local machine and navigating to the project directory make sure to install required packages with:
```
pipenv install
```
Next start a virtual environment with:
```
pipenv shell
```
Navigate to the db directory with:
```
cd lib/db
```
to create the database and data run:
```
alembic upgrade head
```
then run:
```
python db/seed.py
```
to run the CLI app cd back into the lib directory and run:
```
python cli.py
```
