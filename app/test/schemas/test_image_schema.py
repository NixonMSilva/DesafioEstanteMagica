import pytest
import os

from app.schemas.image import Image, ImageInput

# These are the unit tests for the "Image" schema

def test_image_schema():
    image = Image(
        name = "dummy.png",
        data = b"123456"
    )

    assert image.dict() == {
        'name': 'dummy.png',
        'data': b'123456'
    }

# These are the unit tests for the "ImageInput" schema

def test_image_input_schema(books_on_db):
    newImage = Image(
        name="dummy.png",
        data=b"123456"
    )

    image_input = ImageInput(
        image = newImage,
        book_id = books_on_db[0].id
    )

    assert image_input.dict() == {
        "image": {
            "name": "dummy.png",
            "data": b"123456" 
        },
        "book_id": books_on_db[0].id
    }
