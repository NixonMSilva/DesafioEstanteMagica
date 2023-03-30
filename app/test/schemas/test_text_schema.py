import pytest
from app.schemas.text import Text, TextInput

# These are the unit tests for the "Text" schema

def test_text_schema():
    text = Text(
        text = "Lorem ipsum dolor sit amet consectetur adipiscing elit. Morbi ligula magna convallis in dolor sed, feugiat sagittis ipsum."
    )

    assert text.dict() == {
        'text': 'Lorem ipsum dolor sit amet consectetur adipiscing elit. Morbi ligula magna convallis in dolor sed, feugiat sagittis ipsum.'
    }

# These are the unit tests for the "TextInput" schema

def test_text_input_schema(books_on_db):
    newText = Text(
        text = "Lorem ipsum dolor sit amet consectetur adipiscing elit. Morbi ligula magna convallis in dolor sed, feugiat sagittis ipsum."
    )

    text_input = TextInput(
        text = newText,
        book_id = books_on_db[0].id
    )

    assert text_input.dict() == {
        "text": {
            "text": "Lorem ipsum dolor sit amet consectetur adipiscing elit. Morbi ligula magna convallis in dolor sed, feugiat sagittis ipsum."
        },
        "book_id": books_on_db[0].id
    }
