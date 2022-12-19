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
