import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

# book_repo.delete_all()
# author_repo.delete_all()

author_1 = Author ("Terry Pratchett")
# author_repo.save(author_1)

# author_2 = Author("Iain M Banks")
# author_repo.save(author_2)

# author_3 = Author("Chris Beckett")
# author_repo.save(author_3)

# author_4 = Author("Steven Erikson")
# author_repo.save(author_4)

# author_5 = Author("Frank Herbert")
# author_repo.save(author_5)

# book_1 = Book("The Colour of Magic", author_1, "Fantasy", "The first book of the Discworld series. It follows the adventures of an incompetent wizard (Rincewind), a rich tourist (Twoflower), and Twoflower's sentient trunk (the Luggage).", 7, 3, 8)
# book_repo.save(book_1)

# book_2 = Book("The Light Fantastic", author_1, "Fantasy", "The second book in the Discworld series. A direct continuation of The Colour of Magic, following more of Rincewind and Twoflower's adventures in Ankh-Morpork and beyond. This time they're joined by the Cohen the Barbarian.", 5, 3, 8)
# book_repo.save(book_2)

# book_3 = Book("Going Postal", author_1, "Fantasy", "Part of the Discorld series, Going Postal follows the trials and tribulations of Moist von Lipvig, a skilled con-artist who must choose between death, or becoming the Postmaster of Ankh-Morpork's run down postal service.", 5, 3, 8)
# book_repo.save(book_3)

# book_4 = Book("Consider Phlebas", author_2, "Sci-Fi", "The first book in a series of novels about an interstellar post-scarcity society called the Culture. Consider Phlebas revolves around the Idiran-Culture war, following Bora Horza Gobuchul who is an enemy of the Culture.", 1, 4, 9)
# book_repo.save(book_4)

# book_5 = Book("Dark Eden", author_3, "Sci-Fi", "Dark Eden explores the disintegration of a small group of highly inbred people, descendants of two individuals whose spaceship crashed on a rogue planet they call Eden. It is the first book of the Eden trillogy. In 2012 the book won the Arthur C. Clarke Award for best science fiction novel.", 1, 2, 5)
# book_repo.save(book_5)

# book_6 = Book("Gardens of the Moon", author_4, "Fantasy", "The first book in the series, Malazan Book of the Fallen. Gardens of the Moon follows the various struggles for power on an intercontinental region dominated by the Malazan Empire. It is notable for the use of high magic, and unusual plot structure. Gardens of the Moon centres around the Imperial campaign to conquer the city of Darujhistan on the continent of Genabackis.", 8, 5, 10)
# book_repo.save(book_6) 

# book_7 = Book("Deadhouse Gates", author_4, "Fantasy","The second book in the Malazan Book of the Fallen series, Deadhouse Gates follows on from Gardens of the Moon. This book follows the actions of different characters to the first, sometimes spread out across the region by hundreds or thousands of miles. Openning with a cull of the nobility of the Malazan Empire, it follows a rebellion, called the Whirlwind, which is led my a mysterious prophetess", 9, 5, 10)
# book_repo.save(book_7)

# book_8 = Book("Memories of Ice", author_4, "Fantasy", "The third book in the Malazan Book of the Fallen series. The events in this book happen at the same time as the events of Deadhouse Gates. Memories of Ice focuses on the renegade Malazan 2nd Army and their new allies on Genabackis, and their battle with the Pannion Domin, a new power emerging from the south of the continent. It also reveals a great deal more about the gods, ascendants and the history of the Imass, K'Chain Che'Malle and the Tiste races.", 7, 5, 10)
# book_repo.save(book_8)

# book_9 = Book("Dune", author_5, "Sci-Fi", "Dune is set in the distant future amidst a feudal interstellar society in which various noble houses control planetary fiefs. It tells the story of young Paul Atreides, whose family accepts the stewardship of the planet Arrakis. Winner of the inaugural Nebula Award for Best Novel. It is said to the the best-selling science fiction novel of all time.", 10, 4, 9)
# book_repo.save(book_9)

# #
# # print (result.__dict__)

# # author_list = author_repo.select_all()
# # for author in author_list:
# #     print(author.__dict__)
# #     print(author.id)

# result = book_repo.select(19)
# print (result.__dict__)
# print (result.author.__dict__)

# author = author_repo.select(1)
# result = book_repo.books_by_author(author)
# for book in result:
#     print(book.__dict__)
#     print(book.author.__dict__)

author = author_repo.select(3)
author_repo.update(author)
print(author.__dict__)








