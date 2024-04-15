from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Book:
    id: int
    title: str
    author: str
    isbn: int
    theme: str


class Searcher(ABC):
    @abstractmethod
    def search_book(self, author: str, catalog_by_kvothe):
        pass


class SearchByAuthor(Searcher):
    def search_book(self, author: str, catalog_by_kvothe):
        searching_books = []
        for i in catalog_by_kvothe:
            if i.__dict__["author"] == author:
                searching_books.append(i)
            else:
                return "We don't have this book"
        return searching_books


class SearchByTitle(Searcher):
    def search_book(self, title: str, catalog_by_kvothe):
        searching_books = []
        for i in catalog_by_kvothe:
            if i.__dict__["title"] == title:
                searching_books.append(i)
            else:
                return "We don't have this book"
        return searching_books


class SearchByBook(Searcher):
    def search_book(self, book: Book, catalog_by_kvothe):
        searching_books = []
        for i in catalog_by_kvothe:
            if i == book:
                searching_books.append(i)
            else:
                return "We don't have this book"
        return searching_books


class LibraryCatalog:
    def __init__(self, catalog_by_kvothe: None = None):
        if catalog_by_kvothe is None:
            catalog_by_kvothe = []
        self.catalog_by_kvothe = catalog_by_kvothe

    def add_book(self, book: Book):
        self.catalog_by_kvothe.append(book)

    def search_book_from_catalog(self, variable, searcher: Searcher):
        return searcher.search_book(variable, self.catalog_by_kvothe)


class User:
    def __init__(self, name: str, surname: str, birth_year: int):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year


class Member:
    def __init__(self, user: User, borrowed_books=None):
        if borrowed_books is None:
            self.borrowed_books = []
        self.user = user

    def borrow_a_book(self, book: Book):
        self.borrowed_books.append(book)
        return self.borrowed_books

