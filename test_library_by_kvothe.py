import json

import pytest

from library_by_kvothe import Book, LibraryCatalog, SearchByAuthor, SearchByTitle


def test_book_class():
    book = Book(
        id=1,
        title="The name of the wind",
        author="Patrick Rothfuss",
        isbn=12345,
        theme="Fantasy"
    )
    assert book
    assert book.title == "The name of the wind"


def test_library_catalog():
    library_catalog_manager = LibraryCatalog()

    assert library_catalog_manager


def test_add_book_to_catalog():
    book_2 = Book(
        id=3,
        title="The name of the wind",
        author="Patrick Rothfuss",
        isbn=12345,
        theme="Fantasy"
    )
    library_catalog_manager = LibraryCatalog()
    library_catalog_manager.add_book(book_2)

    assert library_catalog_manager
    assert library_catalog_manager.catalog_by_kvothe[0].title == "The name of the wind"


def test_search_book():
    book_3 = Book(
        id=2,
        title="The name of the wind",
        author="Patrick Rothfuss",
        isbn=12345,
        theme="Fantasy"
    )
    library_catalog_manager = LibraryCatalog()
    library_catalog_manager.add_book(book_3)

    searcher = SearchByAuthor()
    searcher.search_book("Patrick", library_catalog_manager.catalog_by_kvothe)


def test_search_book_by_author():
    book_4 = Book(
        id=4,
        title="The name of the wind",
        author="Patrick Rothfuss",
        isbn=125445,
        theme="Fantasy"
    )
    library_catalog_manager = LibraryCatalog()
    library_catalog_manager.add_book(book_4)

    author_searcher = SearchByAuthor()
    searching_book = library_catalog_manager.search_book_from_catalog("Patrick Rothfuss", author_searcher)
    assert book_4 in searching_book


def test_search_book_by_title():
    book_5 = Book(
        id=4,
        title="The name of the wind",
        author="Patrick Rothfuss",
        isbn=125445,
        theme="Fantasy"
    )
    library_catalog_manager = LibraryCatalog()
    library_catalog_manager.add_book(book_5)

    title_searcher = SearchByTitle()
    searching_book = library_catalog_manager.search_book_from_catalog("The name of the wind", title_searcher)
    assert book_5 in searching_book
