class Ebook:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
        self.book_opened = False

    def open_book(self):
        self.book_opened = True

    def close_book(self):
        self.book_opened = False

    def read(self):
        if self.book_opened == True:
            new_page = self.current_page + 1
            if new_page >= 0 and new_page <= self.pages:
                self.current_page = new_page
        else:
            print("Book is closed")

    def book_status(self):
        print(f"{self.title}, written by {self.author}, pages: {self.pages}. You are at page {self.current_page}")
