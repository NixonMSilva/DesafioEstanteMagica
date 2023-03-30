from app.schemas.base import CustomBaseModel

class Text(CustomBaseModel):
    text: str

class TextInput(CustomBaseModel):
    text: Text
    book_id: int