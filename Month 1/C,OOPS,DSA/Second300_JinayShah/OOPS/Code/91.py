class Author:
  def __init__(self, name):
      self.name = name

class Book:
  def __init__(self, title, author):
      self.title = title
      self.author = author
      self.is_checked_out = False

class Member:
  def __init__(self, name):
      self.name = name
      self.books_checked_out = []

  def borrow_book(self, book):
      if not book.is_checked_out:
          book.is_checked_out = True
          self.books_checked_out.append(book)
      else:
          print("This book is already checked out.")

  def return_book(self, book):
      if book in self.books_checked_out:
          book.is_checked_out = False
          self.books_checked_out.remove(book)
      else:
          print("You didn't borrow this book.")

class Library:
  def __init__(self):
      self.members = []
      self.books = []

  def add_member(self, member):
      self.members.append(member)

  def add_book(self, book):
      self.books.append(book)

author1 = Author('Author1')

book1 = Book('Book1', author1)

library1 = Library()

library1.add_book(book1)

member1 = Member('John')

library1.add_member(member1)

member1.borrow_book(book1)

print(member1.name, " borrowed books:", member1.books_checked_out[0].title)
