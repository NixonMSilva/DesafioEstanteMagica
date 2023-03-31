from app.db.models import Book as BookModel
from app.main import app

from fastapi.testclient import TestClient
from fastapi import status

client = TestClient(app)

# This test tests the route for adding new books

def test_add_book_route(db_session):

    # The magic key will have a placeholder here
    # because its generation happens on the back-end
    body = {
        "name": "O Pequeno Príncipe",
        "author": "Antoine de Saint-Exupéry",
        "teacher": "Maria de Sá",
    }

    response = client.post('/book/add', json=body)

    assert response.status_code == status.HTTP_201_CREATED

    books_on_db = db_session.query(BookModel).all()

    assert len(books_on_db) == 1

    db_session.delete(books_on_db[0])
    db_session.commit()

# This test tests the route for searching books by an existing magic key

def test_search_book_by_magic_key_route(db_session, books_on_db):

    response = client.get('/book/list/ABCDEF')

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert data['book']['name'] == "O Pequeno Príncipe"
    assert data['book']['author'] == "Antoine de Saint-Exupéry"
    assert data['book']['teacher'] == "Maria de Sá"
    assert data['book']['magic_key'] == "ABCDEF"

# This test tests the route for searching books by an invalid magic key

def test_search_book_by_magic_key_route_invalid(db_session, books_on_db):

    response = client.get('/book/list/ZZZZZZ')

    assert response.status_code == status.HTTP_404_NOT_FOUND