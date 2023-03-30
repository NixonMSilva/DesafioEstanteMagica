import pytest

from app.db.connection import Session
from app.db.models import Book as BookModel
from app.db.models import Text as TextModel
from app.db.models import Image as ImageModel

# This fixture initializes a session with the database
# on demand during the execution of the tests
@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()

# This fixture initializes some books on the database
# in order to help validate certain unit tests
@pytest.fixture()
def books_on_db(db_session):
    books = [
        BookModel(name="O Pequeno Príncipe", author="Antoine de Saint-Exupéry", teacher="Maria de Sá", magic_key="ABCDEF"),
        BookModel(name="O Menino Maluquinho", author="Ziraldo", teacher="Sofia Pereira", magic_key="AEIOUZ"),
        BookModel(name="Alice no País das Maravilhas", author="Lewis Carroll", teacher="Joana Almeida", magic_key="XIZBQR")
    ]

    for book in books:
        db_session.add(book)
    db_session.commit()

    for book in books:
        db_session.refresh(book)

    yield books

    for book in books:
        db_session.delete(book)
    db_session.commit()