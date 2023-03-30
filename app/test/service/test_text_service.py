import pytest

from app.db.models import Text as TextModel
from app.schemas.book import Book
from app.schemas.text import Text
from app.service.text import TextServices

from fastapi.exceptions import HTTPException

# This test tests adding a text to an existing book

def test_add_text_existing_book(db_session, books_on_db):
    service = TextServices(db_session)

    text = Text(
        text = "Lorem ipsum dolor sit amet consectetur adipiscing elit. Morbi ligula magna convallis in dolor sed, feugiat sagittis ipsum."
    )

    service.add_text(text=text, book_id=books_on_db[0].id)

    text_on_db = db_session.query(TextModel).first()

    assert text_on_db is not None
    assert text_on_db.text == "Lorem ipsum dolor sit amet consectetur adipiscing elit. Morbi ligula magna convallis in dolor sed, feugiat sagittis ipsum." 
    assert text_on_db.book_id == books_on_db[0].id

    db_session.delete(text_on_db)
    db_session.commit()

# This test tests adding a text to an invalid book

def test_add_text_invalid_book(db_session):
    service = TextServices(db_session)

    text = Text(
        text = "Lorem ipsum dolor sit amet consectetur adipiscing elit. Morbi ligula magna convallis in dolor sed, feugiat sagittis ipsum."
    )

    with pytest.raises(HTTPException):
        service.add_text(text=text, book_id=-1)

# This test tests adding a text to a book until it's
# saturated, i.e., reaching its text limit

def test_add_text_saturate_book(db_session, books_on_db):
    service = TextServices(db_session)

    test_text = "Lorem ipsum dolor sit amet consectetur"
    texts = test_text.split(" ")

    for curr_text in texts:
        service.add_text(Text(text=curr_text), book_id=books_on_db[0].id)
    
    # When adding the seventh text expect an error
    with pytest.raises(HTTPException):
        service.add_text(Text(text="adipiscing"), book_id=books_on_db[0].id)
    

    # Delete all texts added to the database
    texts_on_db = db_session.query(TextModel).all()

    for text_on_db in texts_on_db:
        db_session.delete(text_on_db)

    db_session.commit()