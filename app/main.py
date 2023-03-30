from fastapi import FastAPI

from app.routes.book_routes import router as book_routes
from app.routes.text_routes import router as text_routes
from app.routes.image_routes import router as image_routes

app = FastAPI()

@app.get('/health-check')
def health_check():
    return True

app.include_router(book_routes)
app.include_router(text_routes)
app.include_router(image_routes)