from graphene_django.types import DjangoObjectType
from .models import Author,Book, Editorial


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        field = ('name','last_name','genre','summary','is_active','birth_day')
  

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        field = ('titule','summary','date_created')


class EditorialType(DjangoObjectType):
    class Meta:
        model = Editorial
        field = ('name','genre','summary',)