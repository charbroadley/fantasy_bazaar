import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

author_repo.delete_all()
book_repo.delete_all()

author_1 = Author ('Terry Pratchett')
author_repo.save(author_1)

book_1 = Book('The Colour of Magic', author_1, 'Fantasy', 'Sample description: bffege jytjheh sdfsd rt adhrh dsdvsd jyj sd ht sfer gegeh jhfufriu wieuyu edw feerger wdxw juujyj vrtrtvtrt  grg rr e wv  e tthhr yrtuguyg yguyhbb rd rdrd bjhbhb kl dxd uuyiu', 7, 3, 8)
book_repo.save(book_1)