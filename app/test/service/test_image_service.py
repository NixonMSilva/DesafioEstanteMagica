import pytest

from app.db.models import Image as ImageModel
from app.schemas.book import Book
from app.schemas.image import Image
from app.service.image import ImageServices

from fastapi.exceptions import HTTPException

# This test tests adding an image to an existing book

def test_add_image_existing_book(db_session, books_on_db):
    service = ImageServices(db_session)

    image = Image(
        name = "dummy.png",
        data = b"123456"
    )

    service.add_image(image=image, book_id=books_on_db[0].id)

    image_on_db = db_session.query(ImageModel).first()

    assert image_on_db is not None
    assert image_on_db.name == "dummy.png"
    assert image_on_db.data == b"123456"
    assert image_on_db.book_id == books_on_db[0].id

    db_session.delete(image_on_db)
    db_session.commit()

# This test tests adding an image to an invalid book

def test_add_image_invalid_book(db_session):
    service = ImageServices(db_session)

    image = Image(
        name = "dummy.png",
        data = b"123456"
    )

    with pytest.raises(HTTPException):
        service.add_image(image=image, book_id=-1)

# This test tests adding images to a book until it's
# saturated, i.e., reaching its image limit

def test_add_image_saturate_book(db_session, books_on_db):
    service = ImageServices(db_session)

    image = Image(
        name = "dummy.png",
        data = b"123456"
    )

    for i in range(6):
        service.add_image(image=image, book_id=books_on_db[0].id)
    
    # When adding the seventh text expect an error
    with pytest.raises(HTTPException):
        service.add_image(image=image, book_id=books_on_db[0].id)
    

    # Delete all texts added to the database
    images_on_db = db_session.query(ImageModel).all()

    for image_on_db in images_on_db:
        db_session.delete(image_on_db)

    db_session.commit()