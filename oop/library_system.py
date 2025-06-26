class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author


class EBook(Book):
    def __init___(self,file_size):
        self.file_size = file_size


class PrintBook(Book):
    def __init___(self,page_count):
        self.page_count = page_count

class Library(EBook,PrintBook):

    def add_book(self,book):
        self.book = append()

    def list_books(self):
        pass
        
    
