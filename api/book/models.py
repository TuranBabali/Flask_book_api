from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Column, Integer, String, ForeignKey,Text

from api import db

class Book(db.Model):

    __tablename__ = 'books'

    id:Mapped[int] = mapped_column(Integer,primary_key=True)

    name: Mapped[str] = mapped_column(String(100),nullable= False)

    def __repr__(self):
        return self.name