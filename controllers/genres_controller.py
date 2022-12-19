from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from models.author import Author
import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

genres_blueprint = Blueprint("genres", __name__)

@genres_blueprint.route("/genres")
def genres ():
    return render_template("genres/index.html")

# genres/fantasy - with list of all fantasy books
@genres_blueprint.route("/genres/fantasy")
def fantasy ():
    fantasy_books = book_repo.books_by_genre_fantasy()
    return render_template("genres/fantasy.html", fantasy_books = fantasy_books)

# genres/sci-fi - with list of all sci-fi books
@genres_blueprint.route("/genres/sci-fi")
def scifi ():
    scifi_books = book_repo.books_by_genre_scifi()
    return render_template("genres/sci-fi.html", scifi_books = scifi_books)

