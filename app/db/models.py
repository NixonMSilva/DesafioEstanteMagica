from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    author = Column('author', String, nullable=False)
    teacher = Column('teacher', String, nullable=False)
    magic_key = Column('magic_key', String, nullable=False, unique=True)

    texts = relationship('Text', back_populates='book')
    images = relationship('Image', back_populates='book')

class Text(Base):
    __tablename__ = 'texts'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    text = Column('name', String, nullable=False)
    book_id = Column('book_id', ForeignKey('books.id'), nullable=False)

    book = relationship('Book', back_populates='texts')

class Image(Base):
    __tablename__ = 'images'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    data = Column('data', LargeBinary, nullable=False)
    book_id = Column('book_id', ForeignKey('books.id'), nullable=False)

    book = relationship('Book', back_populates='images')