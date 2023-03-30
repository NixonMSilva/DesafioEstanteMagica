from app.routes.deps import get_db_session
from app.schemas.image import Image, ImageInput
from app.service.image import ImageServices

from typing import Annotated
from fastapi import APIRouter, File, Form, UploadFile, Depends, Response, status

from sqlalchemy.orm import Session

router = APIRouter(prefix='/image', tags=['Image'])

@router.post('/add/')
async def add_image(
    file: Annotated[UploadFile, File()],
    book_id: Annotated[int, Form()],
    db_session: Session = Depends(get_db_session)
):
    
    filename = ""
    if (file.filename is None):
        filename = "placeholder.png"
    else:
        filename = file.filename

    image_data = await file.read()

    image = Image(
        name = filename,
        data = image_data
    )

    image_input = ImageInput(
        image = image,
        book_id = book_id
    )

    service = ImageServices(db_session=db_session)
    service.add_image(
        image=image_input.image,
        book_id=image_input.book_id
    )

    return Response(status_code=status.HTTP_201_CREATED)