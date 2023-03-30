from app.schemas.base import CustomBaseModel

class Image(CustomBaseModel):
    name: str
    data: bytes

class ImageInput(CustomBaseModel):
    image: Image
    book_id: int