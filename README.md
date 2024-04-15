### LIBRARY BY KVOTHE

#### Opis zadania z cyklu wyzwania w PyMasters:
Wyobraź sobie, że tworzysz system do zarządzania biblioteką książek. System powinien umożliwić dodawanie książek
do katalogu, wyszukiwanie książek po różnych kryteriach oraz wypożyczanie i zwracanie książek przez użytkowników.
Twoim zadaniem jest zaprojektowanie i zaimplementowanie podstawowych komponentów tego systemu,
przestrzegając zasad SOLID.

#### Rozwiąznie
Nie jest to dopracowane rozwiązanie z uwagi na brak czasu, jednak starałem się 
zawrzeć w kodzie elementy SOLID. Brakuje więcej wariantów, opcji, testów. 

1. Single Responsibility
---

- Klasa Book - odpowiada tylko za przechowywanie danych o książce
   ```python
   @dataclass
   class Book:
       id: int
       title: str
       author: str
       isbn: int
       theme: str 
   ```
- Klasa LibraryCatalog - odpowiada za obsługę katalogu z książkami (dodawanie, wyszukiwanie, ...)
    ```python
    class LibraryCatalog:
        def __init__(self):
            pass

        def add_book(self):
            pass

        def search_book_from_catalog(self):
            pass
   ```
----
2. Open/Closed
- Mamy tu klasy odpowiedzialne za szukanie książek po różnych elemntach (po autorze, tytule)
wszystkich informacjach), ale też jesteśmy otwarci na dodanie opcji szukania po id
```python
class Searcher(ABC):

    @abstractmethod
    def search_book(self):
        pass

class SearchByAuthor(Searcher):
    def search_book(self):
        pass

class SearchByTitle(Searcher):
    def search_book(self):
        pass
```
---
3. Liskov Substitution
  - Zaimplementowałem klasę Member, która w konstruktorze przyjmuje klasę User dzięki czemu jest odporna na zmiany pól w userze.
```python
class User:
    def __init__(self, name: str, surname: str, birth_year: int):
        pass


class Member:
    def __init__(self, user: User, borrowed_books=None):
        pass
    def borrow_a_book(self, book: Book):
        pass
```
4. Interface Segregation - czy można tu podpiąć kwestię różnych klas odpowiedzialnych za szukanie
---
5. Dependency Inversion
  - za searcher podstawiamy interfejs Searcher, dzięki czemu "nie interesują nas" szczegóły implementacyjne
```python
def search_book_from_catalog(self, variable, searcher: Searcher):
    return searcher.search_book(variable, self.catalog_by_kvothe)

```
---
W pliku test_library_by_kvothe są zawarte testy, które uruchamiamy poprzez
```python
pytest -vv
```

