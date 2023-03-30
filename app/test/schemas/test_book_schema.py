import pytest
from app.schemas.book import Book

# These are the unit tests for the "Book" schema

def test_book_schema():
    book = Book(
        name = "O Pequeno Príncipe",
        author = "Antoine de Saint-Exupéry",
        teacher = "Maria de Sá",
        magic_key = "ABCDEF"
    )

    assert book.dict() == {
        'name': 'O Pequeno Príncipe',
        'author': 'Antoine de Saint-Exupéry',
        'teacher': 'Maria de Sá',
        'magic_key': 'ABCDEF'
    }

def test_book_schema_invalid_magic_key():
    with pytest.raises(ValueError):
        book = Book(
            name = "O Pequeno Príncipe",
            author = "Antoine de Saint-Exupéry",
            teacher = "Maria de Sá",
            magic_key = "aBCDEF"
        )
    
    with pytest.raises(ValueError):
        book = Book(
            name = "O Pequeno Príncipe",
            author = "Antoine de Saint-Exupéry",
            teacher = "Maria de Sá",
            magic_key = "1BCDEF"
        )
    
    with pytest.raises(ValueError):
        book = Book(
            name = "O Pequeno Príncipe",
            author = "Antoine de Saint-Exupéry",
            teacher = "Maria de Sá",
            magic_key = "$BCDEF"
        )