from p9 import Book


class Ebook(Book):

    def __init__(self, author, title, file):
        super().__init__(author, title)
        self.file = file

    def __str__(self):
        return f"Author: {self.author}\nTitle: {self.title}\nFile name: {self.file}"


ebook = Ebook("Hobbit", "J.R.R Tolkien", "hobbit.txt")
print(ebook)
