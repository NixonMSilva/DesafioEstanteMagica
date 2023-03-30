import pytest

from app.db.models import Book as BookModel
from app.schemas.book import Book, BookOutput
from app.service.book import BookServices

from fastapi.exceptions import HTTPException

# This test tests adding a book with a fixed magic key

def test_add_book_service_fixed_key(db_session):
    service = BookServices(db_session)
    
    book = Book(
        name = "O Pequeno Príncipe",
        author = "Antoine de Saint-Exupéry",
        teacher = "Maria de Sá",
        magic_key = "ABCDEF"
    )

    service.add_book(book=book, should_generate_key=False)

    books_on_db = db_session.query(BookModel).all()
    assert len(books_on_db) == 1
    assert books_on_db[0].name == "O Pequeno Príncipe"
    assert books_on_db[0].author == "Antoine de Saint-Exupéry"
    assert books_on_db[0].teacher == "Maria de Sá"
    assert books_on_db[0].magic_key == "ABCDEF"

    db_session.delete(books_on_db[0])
    db_session.commit()

# This test tests adding a book with a randomly generated magic key 
# that collides with an existing one

def test_add_book_service_existing_key(db_session):
    service = BookServices(db_session)
    
    first_book = Book(
        name = "O Pequeno Príncipe",
        author = "Antoine de Saint-Exupéry",
        teacher = "Maria de Sá",
        magic_key = "ABCDEF"
    )
    second_book = Book(
        name = "O Menino Maluquinho",
        author = "Ziraldo",
        teacher = "Sofia Pereira",
        magic_key = "ABCDEF"
    )

    service.add_book(book=first_book, should_generate_key=False)

    with pytest.raises(HTTPException):
        service.add_book(book=second_book, should_generate_key=False)

    books_on_db = db_session.query(BookModel).all()

    assert len(books_on_db) == 1

    db_session.delete(books_on_db[0])
    db_session.commit()

# This test tests searching for a book based on a magic key
# it uses a fixture that generates automatically three books
# for testing purposes

def test_search_book_by_magic_key(db_session, books_on_db):
    service = BookServices(db_session)

    right_book = service.search_book_by_magic_key('ABCDEF')
    assert right_book is not None
    assert right_book.book.name == "O Pequeno Príncipe"
    assert right_book.book.author == "Antoine de Saint-Exupéry"
    assert right_book.book.teacher == "Maria de Sá"

    with pytest.raises(HTTPException):
        service.search_book_by_magic_key('KAMWFG')