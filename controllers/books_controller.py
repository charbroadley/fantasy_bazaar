from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

bookshop_blueprint = Blueprint("books", __name__)

@bookshop_blueprint.route("/")
def index ():
    return render_template("index.html", title='Fantasy Bazaar')

@bookshop_blueprint.route("/books")
def bookshop_index ():
    bookshop = book_repo.select_all()
    return render_template("books/index.html", title = 'Stock', all_books = bookshop)

