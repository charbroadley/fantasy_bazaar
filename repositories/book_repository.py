from db.run_sql import run_sql
from models.book import Book
from models.author import Author
import repositories.author_repository as author_repo

def save (book):
    sql = "INSERT INTO BOOKS (title, author_id, genre, description, stock_quantity, buying_cost, selling_price) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.genre, book.description, book.stock_quantity, book.buying_cost, book.selling_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all ():
    books = []
    sql = "SELECT * FROM books"
    results =run_sql (sql)

    for row in results:
        author = author_repo.select(row['author_id'])
        book = Book(row['title'], author, row['genre'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'])
        books.append(book)
    return books

def delete_all ():
    sql = "DELETE FROM books"
    run_sql(sql)