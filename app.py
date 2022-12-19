from flask import Flask, render_template

from controllers.books_controller import bookshop_blueprint
from controllers.authors_controller import authors_blueprint
from controllers.genres_controller import genres_blueprint

app = Flask(__name__)

app.register_blueprint(bookshop_blueprint)
app.register_blueprint(authors_blueprint)
app.register_blueprint(genres_blueprint)



@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)