class Book:
<<<<<<< HEAD
    def __init__(self, title, author):
        
    self.title = title
    self.author = author
    check_out_book = title
    return_book = title
    list_available_books
    
=======
    def __init__(self, title, author):     
      self.title = title
      self.author = author
      self._is_checked_out = False

    def check_out_book(self, title):
        self._is_checked_out = True

    def return_book(self):
        self.return_ = False

    def list_available_books(self):
        return not self._is_checked_out
    
class Library:
    def __init__(self):
      self._books = []

     def add_book(self):
        self.add_ = __books.append(Book())

     def check_out_book(self, title):
         pass

     def return_book(self, title):
         self.return_ = __books.remove(Book())

     def list_available_books(self):
         print("My available books: ",__books)
         
>>>>>>> 2e8d96802e3047d551461f6612c2255b0177efb5
