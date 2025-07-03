class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

class EBook(Book):
    def __init___(self,file_size):
        super().__init___(title)
        self.file_size = file_size
        


class PrintBook(Book):
    def __init___(self,page_count):
        self.page_count = page_count

class Library(EBook,PrintBook):
    self.books = []

    def add_book(self,book):
        self.book = append()

    def list_books(self):
        pass
        
book = Book(Library())
book.add_book()
