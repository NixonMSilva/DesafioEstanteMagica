from app.db.models import Book as BookModel
from app.db.models import Image as ImageModel
from app.schemas.image import Image
from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

class ImageServices:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    # Service for adding images

    def add_image(self, image: Image, book_id: int):

        # Checks if the book with the specified id exists
        book = self.db_session.query(BookModel).filter_by(id=book_id).first()
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No book was found with id {book_id}')
        
        # Checks if the specified book isn't full of images
        if self.check_image_limit(book_id=book_id, image_limit=6):
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f'Book with id {book_id} has too many texts already')

        image_model = ImageModel(**image.dict())
        image_model.book_id = book.id

        self.db_session.add(image_model)
        self.db_session.commit()
    
    # Service for listing images from a certain book
    def list_images_by_book(self, book_id: int):
        # Build the images array
        images_on_db = self.db_session.query(ImageModel).filter_by(book_id=book_id).all()

        images = [
            self._serialize_image(image_on_db)
            for image_on_db in images_on_db
        ]
        return images
    
    def _serialize_image(self, images_on_db: ImageModel):
        image_dict = dict(name = images_on_db.name, data = str(images_on_db.data))
        return Image(**image_dict)
     
    
    def check_image_limit(self, book_id: int, image_limit: int):

        # Checks if the book has filled the limit of six texts or not
        images_by_book = self.db_session.query(ImageModel).filter_by(book_id=book_id).all()

        if len(images_by_book) >= image_limit:
            return True
        
        return False
