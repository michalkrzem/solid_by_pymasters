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
        return searching_books


class SearchByTitle(Searcher):
    def search_book(self, title: str, catalog_by_kvothe):
        searching_books = []
        for i in catalog_by_kvothe:
            if i.__dict__["title"] == title:
                searching_books.append(i)
        return searching_books


class LibraryCatalog:
    def __init__(self, catalog_by_kvothe=None):
        if catalog_by_kvothe is None:
            catalog_by_kvothe = []
        self.catalog_by_kvothe = catalog_by_kvothe
        print(self.catalog_by_kvothe)

    def add_book(self, book: Book):
        self.catalog_by_kvothe.append(book)

    def search_book_from_catalog(self, variable, searcher: Searcher):
        return searcher.search_book(variable, self.catalog_by_kvothe)

