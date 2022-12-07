from ebook import Ebook

ebook = Ebook("Hobbit", "J.R.R Tolkien", 450)
ebook.open_book()
ebook.book_status()

i = 0
while i < 30:
    ebook.read()
    i += 1

ebook.book_status()
ebook.close_book()
ebook.read()
ebook.book_status()
