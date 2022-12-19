from db.run_sql import run_sql
from models.book import Book
from models.author import Author
import repositories.author_repository as author_repo

def save (book):
    sql = "INSERT INTO books (title, author_id, genre, description, stock_quantity, buying_cost, selling_price) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.genre, book.description, book.stock_quantity, book.buying_cost, book.selling_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all ():
    books = []
    sql = "SELECT * FROM books ORDER BY title ASC"
    results =run_sql (sql)

    for row in results:
        author = author_repo.select(row['author_id'])
        book = Book(row['title'], author, row['genre'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['id'])
        books.append(book)
    return books

def select (id):
    book = None
    sql = "SELECT * FROM books WHERE id =%s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results [0]
        author = author_repo.select(result['author_id'])
        book = Book(result['title'], author, result['genre'], result['description'], result['stock_quantity'], result['buying_cost'], result['selling_price'], result['id'])
    return book

def update (book):
    sql = "UPDATE books SET (title, author_id, genre, description, stock_quantity, buying_cost, selling_price) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [book.title, book.author.id, book.genre, book.description, book.stock_quantity, book.buying_cost, book.selling_price, book.id]
    run_sql(sql, values)

# find all books by an author
def books_by_author (author):
    books = []
    sql = "SELECT * FROM books WHERE author_id = %s"
    values = [author.id]
    results = run_sql (sql, values)

    for row in results:
        book = Book(row['title'], author, row['genre'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['id'])
        books.append(book)
    return books

def books_by_genre_fantasy ():
    books = []
    sql = "SELECT * FROM books WHERE genre = 'Fantasy'"
    results = run_sql(sql)

    for row in results:
        book = Book(row['title'], row['author_id'], row['genre'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['id'])
        books.append(book)
    return books

def books_by_genre_scifi ():
    books = []
    sql = "SELECT * FROM books WHERE genre = 'Sci-Fi'"
    results = run_sql(sql)

    for row in results:
        book = Book(row['title'], row['author_id'], row['genre'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['id'])
        books.append(book)
    return books



def delete (id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def delete_all ():
    sql = "DELETE FROM books"
    run_sql(sql)