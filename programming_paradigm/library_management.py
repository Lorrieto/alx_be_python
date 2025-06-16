class Book:
    def __init__(self,title,author):     
      self.title = title
      self.author = author
      __is_checked_out = False

    def check_out_book(self, title):
        pass

    def return_book(self, title, author):
        self.return_ = remove(Book(title, author))

    def list_available_books(self):
        print()
    
class Library:
     __books = []

     def add_book(self):
        self.add_ = __books.append(Book())

     def check_out_book(self, title):
         pass

     def return_book(self, title):
         self.return_ = __books.remove(Book())

     def list_available_books(self):
         print("My available books: ",__books)
         
