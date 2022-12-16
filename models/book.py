class Book:
    def __init__(self, title, author, genre, description, stock_quantity, buying_cost, selling_price, id = None):
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.id = id