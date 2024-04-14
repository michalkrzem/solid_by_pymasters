import pytest

from library_by_kvothe import Book


def test_book_class():
    book = Book(
        title="Name of the wind",
        autor="Patrik Roofus",
        isbn=12345,
        theme="Fantasy"
    )
    assert book
    assert book.title == "Name of the wind"
