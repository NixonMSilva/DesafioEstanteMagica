import random
import string

from app.db.models import Book as BookModel
from app.schemas.book import Book, BookInput, BookOutput
from app.service.text import TextServices
from app.service.image import ImageServices
from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

class BookServices:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    # Service for adding books via the router (BookInput instead of Book)
    def add_book_input (self, book_input: BookInput):
        book = Book(
            name=book_input.name,
            author=book_input.author,
            teacher=book_input.teacher,
            magic_key="PLACEH"
        )
        self.add_book(book=book, should_generate_key=True)

    # Service for finally adding books
    def add_book(self, book: Book, should_generate_key: bool):
        book_model = BookModel(**book.dict())

        if should_generate_key:
            book_model.magic_key = self.generate_magic_key(6, 256)
            if book_model.magic_key == "X":
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
        if not self.validate_magic_key(book_model.magic_key):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        self.db_session.add(book_model)
        self.db_session.commit()
    
    # Service for searching books by magic key

    def search_book_by_magic_key (self, magic_key: str):
        text_services = TextServices(db_session=self.db_session)
        image_services = ImageServices(db_session=self.db_session)

        requested_book = self.db_session.query(BookModel).filter_by(magic_key=magic_key).first()

        if not requested_book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        
        text_list = text_services.list_texts_by_book(requested_book.id)
        image_list = image_services.list_images_by_book(requested_book.id)

        book_output = BookOutput(
            book=requested_book.__dict__,
            texts=text_list,
            images=image_list
        )

        return book_output
    
    def validate_magic_key(self, magic_key: str):
        existing_magic_key = self.db_session.query(BookModel).filter_by(magic_key=magic_key).first()
        # If magic key doesn't exist then it's valid, if it does, then it's not
        if not existing_magic_key:
            return True
        return False
    
    def generate_magic_key(self, length: int, max_attemps: int):
        letters = string.ascii_uppercase
        magic_key = ''.join(random.choice(letters) for i in range(length))

        # Try 'max_attempts' times in order to not make the server get stuck in
        # an infinite loop in worst case scenario -> All valid magic_keys
        # have been used OR 'max_attempts' attempts weren't enough to randomly
        # generate a valid magic key
        for i in range(max_attemps):
            if self.validate_magic_key(magic_key):
                return magic_key
        
        return "X"
    
        

    
