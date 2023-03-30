from app.routes.deps import get_db_session
from app.schemas.text import Text, TextInput
from app.service.text import TextServices

from fastapi import APIRouter, Depends, Response, status

from sqlalchemy.orm import Session

router = APIRouter(prefix='/text', tags=['Text'])

@router.post('/add')
def add_text(
    text_input: TextInput,
    db_session: Session = Depends(get_db_session)
):
    service = TextServices(db_session=db_session)
    service.add_text(
        text=text_input.text, 
        book_id=text_input.book_id
    )

    return Response(status_code=status.HTTP_201_CREATED)