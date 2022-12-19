from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

bookshop_blueprint = Blueprint("books", __name__)

@bookshop_blueprint.route("/")
def index ():
    bookshop = book_repo.select_all()
    return render_template("index.html", all_books = bookshop)

@bookshop_blueprint.route("/books")
def bookshop_index ():
    bookshop = book_repo.select_all()
    return render_template("books/index.html", all_books = bookshop)

# Page for form to add new book - got to have link to all_books so we can access authors in drop down box
@bookshop_blueprint.route("/books/new")
def new():
    author_list = author_repo.select_all()
    return render_template("/books/new.html", all_authors = author_list)

# to save the info from the add new book form - not a new page
@bookshop_blueprint.route("/books", methods = ['POST'])
def create ():
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']

    author = author_repo.select(author_id)
    book = Book (title, author, genre, description, stock_quantity, buying_cost, selling_price)
    book_repo.save(book)
    return redirect("/books")

# to see a single book page
@bookshop_blueprint.route("/books/<id>")
def show (id):
    book = book_repo.select(id)
    return render_template("/books/show.html", book = book)

# display a form to input changes - got to have link to all_books so we can access authors in drop down box
@bookshop_blueprint.route("/books/<id>/edit")
def edit (id):
    book = book_repo.select(id)
    author_list = author_repo.select_all()
    return render_template("/books/edit.html", book = book, all_authors = author_list)

# to save the info from the edit book form - not a new page
@bookshop_blueprint.route("/books/<id>", methods=["POST"])
def update (id):
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']

    author = author_repo.select(author_id)
    book = Book (title, author, genre, description, stock_quantity, buying_cost, selling_price, id)
    book_repo.update(book)
    return redirect("/books")

# delete just needs a button - maybe add a confirmation page later
@bookshop_blueprint.route("/books/<id>/delete", methods=["POST"])
def destroy (id):
    book_repo.delete(id)
    return redirect("/books")



