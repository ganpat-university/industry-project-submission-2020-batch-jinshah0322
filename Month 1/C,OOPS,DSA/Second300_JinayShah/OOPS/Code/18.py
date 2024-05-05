from typing import List

class Book:
    def __init__(self, book_id: int, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author

class Patron:
    def __init__(self, patron_id: int, name: str):
        self.patron_id = patron_id
        self.name = name

class ISBN:
    def __init__(self, isbn: str):
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book_id: int, title: str, author: str):
        book = Book(book_id, title, author)
        self.books[book_id] = book

    def add_patron(self, patron_id: int, name: str):
        patron = Patron(patron_id, name)
        self.patrons[patron_id] = patron

    def lend_book(self, book_id: int, patron_id: int):
        book = self.books.get(book_id)
        patron = self.patrons.get(patron_id)

        if book and patron:
            print(f"Book '{book.title}' lent to {patron.name}.")
        else:
            print("Book or patron not found.")

class LibraryRepository:
    def __init__(self):
        self.library = Library()

    def save_book(self, book_id: int, title: str, author: str):
        self.library.add_book(book_id, title, author)

    def save_patron(self, patron_id: int, name: str):
        self.library.add_patron(patron_id, name)


library_repo = LibraryRepository()

library_repo.save_book(1, "The Great Gatsby", "F. Scott Fitzgerald")
library_repo.save_book(2, "To Kill a Mockingbird", "Harper Lee")
library_repo.save_patron(101, "John Doe")
library_repo.save_patron(102, "Jane Doe")

library_repo.library.lend_book(1, 101)
