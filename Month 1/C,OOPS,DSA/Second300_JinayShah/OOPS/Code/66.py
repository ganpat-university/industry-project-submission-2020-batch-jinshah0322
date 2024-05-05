class Book:
   def __init__(self, title, author, id):
       self.title = title
       self.author = author
       self.id = id
       self.checked_out = False

   def checkout(self):
       self.checked_out = True

   def return_book(self):
       self.checked_out = False

class Author:
   def __init__(self, name):
       self.name = name
       self.books = []

   def add_book(self, book):
       self.books.append(book)

class Library:
   def __init__(self):
       self.books = []
       self.overdue_fines = {}

   def add_book(self, book):
       self.books.append(book)

   def checkout_book(self, id):
       for book in self.books:
           if book.id == id and not book.checked_out:
               book.checkout()
               return f"Book with ID {id} checked out."
       return "Book not found or already checked out."

   def return_book(self, id):
       for book in self.books:
           if book.id == id and book.checked_out:
               book.return_book()
               return f"Book with ID {id} returned."
       return "Book not found or not checked out."

   def add_overdue_fine(self, id, amount):
       if id not in self.overdue_fines:
           self.overdue_fines[id] = amount
       else:
           self.overdue_fines[id] += amount

   def pay_fine(self, id, amount):
       if id in self.overdue_fines and self.overdue_fines[id] >= amount:
           self.overdue_fines[id] -= amount
           return f"Paid fine for book with ID {id}"
       else:
           return "Cannot pay fine for this book."

author1 = Author("Author1")
book1 = Book("Book1", author1, 1)
book2 = Book("Book2", author1, 2)
author1.add_book(book1)
author1.add_book(book2)

library = Library()
library.add_book(book1)
library.add_book(book2)

print(library.checkout_book(1))

print(library.return_book(1))

library.add_overdue_fine(1, 5)

print(library.pay_fine(1, 3))
