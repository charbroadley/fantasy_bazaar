from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from models.author import Author
import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

authors_blueprint = Blueprint("authors", __name__)

@authors_blueprint.route("/authors")
def authors ():
    author = author_repo.select_all()
    return render_template("/authors/index.html", author_list = author)

# to see a single author page - add a function here to see all books by an author
@authors_blueprint.route("/authors/<id>")
def show (id):
    author = author_repo.select(id)
    books = book_repo.books_by_author(author)
    return render_template("/authors/show.html", author = author, book_list = books)

# page for form to add new author
@authors_blueprint.route("/authors/new")
def new():
    return render_template("/authors/new.html")

# to save the info from the add new author form - not a new page
@authors_blueprint.route("/authors", methods =['POST'])
def create ():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    status = request.form['completed']
    author = Author(first_name, last_name, status)
    author_repo.save(author)
    return redirect("/authors")

# page for form to edit author
@authors_blueprint.route("/authors/<id>/edit")
def edit (id):
    author = author_repo.select(id)
    return render_template('/authors/edit.html', author = author)

# to save the changes from the edit author form - not a new page
@authors_blueprint.route("/authors/<id>", methods=['POST'])
def update (id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    status = request.form['status']
    author = Author(first_name, last_name, status, id)
    author_repo.update(author)
    return redirect("/authors")

# delete just needs a button - maybe add a confirmation page later
# @authors_blueprint.route("/authors/<id>/delete", methods=['POST'])
# def destroy (id):
#     author_repo.delete(id)
#     return redirect("/authors")
