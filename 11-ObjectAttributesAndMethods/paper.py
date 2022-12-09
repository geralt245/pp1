from p9 import Book


class PaperBook(Book):

    def __init__(self, author, title, pages):
        super().__init__(author, title)
        self.pages = pages

    def __str__(self):
        return f"Author: {self.author}\nTitle: {self.title}\nNumber of pages: {self.pages}"


book = PaperBook("Hobbit", "J.R.R Tolkien", 432)
print(book)
