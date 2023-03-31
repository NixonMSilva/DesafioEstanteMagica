from app.schemas.book import BookInput
from app.routes.deps import get_db_session
from app.service.book import BookServices

from fastapi import APIRouter, Depends, Response, status, HTTPException

from sqlalchemy.orm import Session

router = APIRouter(prefix='/book', tags=['Book'])

@router.post('/add')
def add_book(
    book: BookInput,
    db_session: Session = Depends(get_db_session)
):
    service = BookServices(db_session=db_session)
    service.add_book_input(book_input=book)

    return Response(status_code=status.HTTP_201_CREATED)

@router.get('/list/{magic_key}')
def search_by_magic_key(
    magic_key: str,
    db_session: Session = Depends(get_db_session)
):
    service = BookServices(db_session=db_session)
    book = service.search_book_by_magic_key(magic_key=magic_key)

    if not book:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND)

    return book