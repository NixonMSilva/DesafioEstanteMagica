import re

from app.schemas.base import CustomBaseModel
from app.schemas.text import Text
from app.schemas.image import Image

from pydantic import validator

from typing import List

class Book(CustomBaseModel):
    name: str
    author: str
    teacher: str
    magic_key: str

    @validator('magic_key')
    def validate_magic_key(cls, value):
        if not re.match('^([A-Z]){6}', value):
            raise ValueError('Invalid magic key')
        return value

class BookInput(CustomBaseModel):
    name: str
    author: str
    teacher: str

class BookOutput(CustomBaseModel):
    book: Book
    texts: List[Text]
    images: List[Image]
