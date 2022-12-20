import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

book_repo.delete_all()
author_repo.delete_all()

author_1 = Author ("Terry", "Pratchett", True)
author_repo.save(author_1)

author_2 = Author("Iain M", "Banks", True)
author_repo.save(author_2)

author_3 = Author("Chris", "Beckett", True)
author_repo.save(author_3)

author_4 = Author("Steven", "Erikson", True)
author_repo.save(author_4)

author_5 = Author("Frank", "Herbert", True)
author_repo.save(author_5)

author_6 = Author("JRR", "Tolkien", True)
author_repo.save(author_6)

author_7 = Author("Jonas", "Eika", True)
author_repo.save(author_7)

author_8 = Author("Andreas", "Eschbach", True)
author_repo.save(author_8)

author_9 = Author("Scott", "Hawkins", False)
author_repo.save(author_9)

author_10 = Author("Andrzej", "Sapkowski", False)
author_repo.save(author_10)

author_11 = Author("Jacqueline", "Harpman", True)
author_repo.save(author_11)

author_12 = Author("Daniel", "Keyes", False)
author_repo.save(author_12)

author_13 = Author("Chuck", "Wendig", True)
author_repo.save(author_13)

author_14 = Author("Iain", "Reid", False)
author_repo.save(author_14)

book_1 = Book("The Colour of Magic", author_1, "Fantasy", "The first book of the Discworld series. It follows the adventures of an incompetent wizard (Rincewind), a rich tourist (Twoflower), and Twoflower's sentient trunk (the Luggage).", 7, 3, 8)
book_repo.save(book_1)

book_2 = Book("The Light Fantastic", author_1, "Fantasy", "The second book in the Discworld series. A direct continuation of The Colour of Magic, following more of Rincewind and Twoflower's adventures in Ankh-Morpork and beyond. This time they're joined by the Cohen the Barbarian.", 5, 3, 8)
book_repo.save(book_2)

book_3 = Book("Going Postal", author_1, "Fantasy", "Part of the Discorld series, Going Postal follows the trials and tribulations of Moist von Lipvig, a skilled con-artist who must choose between death, or becoming the Postmaster of Ankh-Morpork's run down postal service.", 5, 3, 8)
book_repo.save(book_3)

book_4 = Book("Consider Phlebas", author_2, "Sci-Fi", "The first book in a series of novels about an interstellar post-scarcity society called the Culture. Consider Phlebas revolves around the Idiran-Culture war, following Bora Horza Gobuchul who is an enemy of the Culture.", 1, 4, 9)
book_repo.save(book_4)

book_5 = Book("Dark Eden", author_3, "Sci-Fi", "Dark Eden explores the disintegration of a small group of highly inbred people, descendants of two individuals whose spaceship crashed on a rogue planet they call Eden. It is the first book of the Eden trillogy. In 2012 the book won the Arthur C. Clarke Award for best science fiction novel.", 1, 2, 5)
book_repo.save(book_5)

book_6 = Book("Gardens of the Moon", author_4, "Fantasy", "The first book in the series, Malazan Book of the Fallen. Gardens of the Moon follows the various struggles for power on an intercontinental region dominated by the Malazan Empire. It is notable for the use of high magic, and unusual plot structure. Gardens of the Moon centres around the Imperial campaign to conquer the city of Darujhistan on the continent of Genabackis.", 8, 5, 10)
book_repo.save(book_6) 

book_7 = Book("Deadhouse Gates", author_4, "Fantasy","The second book in the Malazan Book of the Fallen series, Deadhouse Gates follows on from Gardens of the Moon. This book follows the actions of different characters to the first, sometimes spread out across the region by hundreds or thousands of miles. Openning with a cull of the nobility of the Malazan Empire, it follows a rebellion, called the Whirlwind, which is led my a mysterious prophetess", 9, 5, 10)
book_repo.save(book_7)

book_8 = Book("Memories of Ice", author_4, "Fantasy", "The third book in the Malazan Book of the Fallen series. The events in this book happen at the same time as the events of Deadhouse Gates. Memories of Ice focuses on the renegade Malazan 2nd Army and their new allies on Genabackis, and their battle with the Pannion Domin, a new power emerging from the south of the continent. It also reveals a great deal more about the gods, ascendants and the history of the Imass, K'Chain Che'Malle and the Tiste races.", 7, 5, 10)
book_repo.save(book_8)

book_9 = Book("Dune", author_5, "Sci-Fi", "Dune is set in the distant future amidst a feudal interstellar society in which various noble houses control planetary fiefs. It tells the story of young Paul Atreides, whose family accepts the stewardship of the planet Arrakis. Winner of the inaugural Nebula Award for Best Novel. It is said to the the best-selling science fiction novel of all time.", 10, 4, 9)
book_repo.save(book_9)

book_10 = Book("The Hobbit", author_6, "Fantasy", "Set within Tolkien's fictional Middle-earth, The Hobbit follows Bilbo Baggins, a home-loving hobbit, in a quest to win a share of the treasure guarded by the dragon Smaug.", 5, 3, 6)
book_repo.save(book_10)

book_11 = Book("The Fellowship of the Ring", author_6, "Fantasy", "The first of The Lord of the Rings trilogy. Young Frodo Baggins finds himself faced with an immense task, after his elderly cousin Bilbo entrusts a ring to his care. Frodo must leave his home and make a perilous journey across Middle-earth to the Cracks of Doom, there to destroy the Ring and foil the Dark Lord in his evil purpose.", 2, 4, 8)
book_repo.save(book_11)

book_12 = Book("The Two Towers", author_6, "Fantasy", "The second installment of The Lord of the Rings Trilogy. Frodo and the Companions of the Ring have been beset by danger during their quest to prevent the Ruling Ring from falling into the hands of Sauron. Now they continue their journey alone down the great River Anduin followed by a mysterious creeping figure that follows wherever they go.", 3, 4, 8)
book_repo.save(book_12)

book_13 = Book("The Return of the King", author_6, "Fantasy", "The third and final volume of The Lord of the Rings. The armies of the Dark Lord are massing as his evil shadow spreads even wider. Men, Dwarves, Elves and Ents unite forces to battle against the Dark. Meanwhile, Frodo and Sam struggle further into Mordor in their heroic quest to destroy the One Ring.", 3, 4, 8)
book_repo.save(book_13)

book_14 = Book("After the Sun", author_7, "Sci-Fi", "Mesmerising and inventive fiction that probes the tender places where human longings push through the cracks of a breaking world. After the Sun opens portals to our newest realities, haunting the margins of a globalised world that’s both saturated with yearning and brutally transactional.", 1, 3, 6)
book_repo.save(book_14)

book_15 = Book("The Hair Carpet Weavers", author_8, "Sci-Fi", "In a distant universe, since the beginning of time, workers have spent their lives weaving intricate carpets from the hair of women and girls. But why? Andreas Eschbach's mysterious, poignant space opera explores the absurdity of work and of life itself.", 1, 3, 6)
book_repo.save(book_15)

book_16 = Book("I Who Have Never Known Men", author_11, "Sci-Fi", "Deep underground, thirty-nine women live imprisoned in a cage. Watched over by guards, the women have no memory of how they got there, no notion of time, and only a vague recollection of their lives before. As the burn of electric light merges day into night and numberless years pass, a young girl—the fortieth prisoner—sits alone and outcast in the corner. Soon she will show herself to be the key to the others’ escape and survival in the strange world that awaits them above ground.", 2, 2, 4)
book_repo.save(book_16)

book_17 = Book("Wanderers", author_13, "Sci-Fi", "An epic tapestry of humanity, told in a chorus of disparate voices, including Shana, a young girl who wakes up one morning to discover her sister in the grip of a strange malady. She appears to be sleepwalking. She cannot talk and cannot be woken up. And she is heading with inexorable determination to a destination that only she knows. But Shana and are sister are not alone. Soon they are joined by a flock of sleepwalkers from across America, on the same mysterious journey. And like Shana, there are other shepherds who follow the flock to protect their friends and family on the long dark road ahead. For on their journey, they will discover an America convulsed with terror and violence, where this apocalyptic epidemic proves less dangerous than the fear of it.", 6, 4, 9)
book_repo.save(book_17)


# print (result.__dict__)

# author_list = author_repo.select_all()
# for author in author_list:
#     print(author.__dict__)
#     print(author.id)

# result = book_repo.select(19)
# print (result.__dict__)
# print (result.author.__dict__)

# author = author_repo.select(1)
# result = book_repo.books_by_author(author)
# for book in result:
#     print(book.__dict__)
#     print(book.author.__dict__)

# author = author_repo.select(3)
# author_repo.update(author)
# print(author.__dict__)

# book_list = book_repo.books_by_genre_fantasy()
# for book in book_list:
#     print(book.__dict__)

# book_list = book_repo.books_by_genre_scifi()
# for book in book_list:
#     print(book.__dict__)

# author_repo.delete(3)











