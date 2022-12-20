from db.run_sql import run_sql
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repo

def save (author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results [0] ['id']
    author.id = id
    return author

def select (id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results [0]
        author = Author(result['name'], result['id'])
    return author

def select_all ():
    authors = []
    sql = "SELECT * FROM authors ORDER BY name ASC"
    results = run_sql (sql)

    for row in results:
        author = Author(row['name'], row['id'])
        authors.append(author)
    return authors

def update (author):
    sql = "UPDATE authors SET name = %s WHERE id = %s"
    values = [author.name, author.id]
    run_sql(sql, values)

# def delete (id):
#     sql = "DELETE  FROM books WHERE id =%s"
#     values = [id]
#     run_sql (sql, values)

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)