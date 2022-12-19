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

# Page for form to add new author
@authors_blueprint.route("/authors/new")
def new():
    return render_template("/authors/new.html")

# to save the info from the add new author form - not a new page
@authors_blueprint.route("/authors", methods =['POST'])
def create ():
    name = request.form['name']
    author = Author(name)
    author_repo.save(author)
    return redirect("/authors")
