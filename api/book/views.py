from flask_restx import Namespace, Resource, fields
from http import HTTPStatus

from .models import Book
from api.database import db

book_namespace = Namespace('book',description="Das ist API für book")
book_model= book_namespace.model(
    'Book',
    {
        'id': fields.Integer(required=True, description='Book ID'),
        'name': fields.String(required=True, description='Book Name'),
    }
    )



@book_namespace.route('/')
class BookGetCreate(Resource):
    def get(self):
        """
        Alle Bücher abrufen
        """
        books= Book.query.all()
        return books, HTTPStatus.OK



    @book_namespace.expect(book_model)
    @book_namespace.marshal_with(book_model)
    def post(self):
        """
        Ein neuer Buch hinzufügen
        """
        data= book_namespace.payload
        print(data,"########")
        name= data['name']
       

        new_book= Book(name=name)
        db.session.add(new_book)
        db.session.commit()

        return new_book, HTTPStatus.CREATED



        