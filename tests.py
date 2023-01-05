import unittest
from models.book import Book
from models.author import Author
import repositories.book_repository as book_repo

class TestBook(unittest.TestCase):

    # def setUp(self):
        # self.author1 = Author ("JRR", "Tolkien", True)
        # self.book1 = Book ("The Hobbit", self.author1, "Fantasy", "Set within Tolkien's fictional Middle-earth, The Hobbit follows Bilbo Baggins, a home-loving hobbit, in a quest to win a share of the treasure guarded by the dragon Smaug.", 5, 3, 6)
        # self.book2 = Book ("The Fellowship of the Ring", self.author1, "Fantasy", "The first of The Lord of the Rings trilogy. Young Frodo Baggins finds himself faced with an immense task, after his elderly cousin Bilbo entrusts a ring to his care. Frodo must leave his home and make a perilous journey across Middle-earth to the Cracks of Doom, there to destroy the Ring and foil the Dark Lord in his evil purpose.", 2, 4, 8)
        # self.book3 = Book ("The Two Towers", self.author1, "Fantasy", "The second installment of The Lord of the Rings Trilogy. Frodo and the Companions of the Ring have been beset by danger during their quest to prevent the Ruling Ring from falling into the hands of Sauron. Now they continue their journey alone down the great River Anduin followed by a mysterious creeping figure that follows wherever they go.", 3, 4, 8)
        # self.book4 = Book ("The Return of the King", self.author1, "Fantasy", "The third and final volume of The Lord of the Rings. The armies of the Dark Lord are massing as his evil shadow spreads even wider. Men, Dwarves, Elves and Ents unite forces to battle against the Dark. Meanwhile, Frodo and Sam struggle further into Mordor in their heroic quest to destroy the One Ring.", 3, 4, 8)

    # def test_book_title (self): 
    #     self.assertEqual ("The Hobbit", self.book1.title)

    def test_filter_books_by_genre_fantasy (self):
        book_list = book_repo.books_by_genre_fantasy ()
        self.assertEqual (len(book_list), 4)

# def books_by_genre_fantasy ():
#     books = []
#     sql = "SELECT * FROM books WHERE genre = 'Fantasy'"
#     results = run_sql(sql)

#     for row in results:
#         author = author_repo.select(row['author_id'])
#         book = Book(row['title'], author, row['genre'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['id'])
#         books.append(book)
#     return books
