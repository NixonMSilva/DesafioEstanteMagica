from app.db.models import Book as BookModel
from app.db.models import Text as TextModel
from app.schemas.text import Text
from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

class TextServices:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    # Service for adding texts

    def add_text(self, text: Text, book_id: int):

        # Checks if the book with the specified id exists
        book = self.db_session.query(BookModel).filter_by(id=book_id).first()
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No book was found with id {book_id}')
        
        # Checks if the specified book isn't full of texts
        if self.check_text_limit(book_id=book_id, text_limit=6):
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f'Book with id {book_id} has too many texts already')

        text_model = TextModel(**text.dict())
        text_model.book_id = book.id

        self.db_session.add(text_model)
        self.db_session.commit()
    
    # Service for listing texts from a certain book
    def list_texts_by_book(self, book_id: int):
        # Build the texts array
        texts_on_db = self.db_session.query(TextModel).filter_by(book_id=book_id).all()

        texts = [
            self._serialize_text(text_on_db)
            for text_on_db in texts_on_db
        ]
        return texts
    
    def _serialize_text(self, texts_on_db: TextModel):
        text_dict = texts_on_db.__dict__
        return Text(**text_dict)
     
    
    def check_text_limit(self, book_id: int, text_limit: int):

        # Checks if the book has filled the limit of six texts or not
        texts_by_book = self.db_session.query(TextModel).filter_by(book_id=book_id).all()

        if len(texts_by_book) >= text_limit:
            return True
        
        return False

