from .types import AuthorType,BookType,EditorialType
from .models import Author, Book, Editorial
import graphene
import datetime

class CreateBookMutation(graphene.Mutation):
    class Arguments:
        titule = graphene.String(required=True)
        summary = graphene.String()

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls,root,info,titule,summary):
        book = Book(
            titule = titule,
            summary = summary)
        book.save()
        
        return CreateBookMutation (book = book)

class UpdateBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        titule = graphene.String(required=True)
        summary = graphene.String()
    
    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls,root,info,id,titule,summary):
        book = Book.objects.get(id=id)
        book.titule = titule
        book.summary = summary
        book.save()

        return UpdateBookMutation(book = book)

class DeleteBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls,root,info,id):
        book = Book.objects.get(id=id)
        book.delete()
        return 
   


class CreateEditorialMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        summary = graphene.String(required=True)
        genre = graphene.String()

    editorial = graphene.Field(EditorialType)
    @classmethod
    def mutate(scl,root,info,name,genre,summary):
        editorial = Editorial(
            name = name,
            genre = genre,
            summary = summary)
        editorial.save()

        return CreateEditorialMutation(editorial = editorial)

class UpdateEditorialMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        summary = graphene.String()
        genre = graphene.String()

    editorial = graphene.Field(EditorialType)

    @classmethod
    def mutate(scl,root,info,id,name,genre,summary):
        editorial = Editorial.objects.get(id=id)
        editorial.name = name,
        editorial.genre = genre,
        editorial.summary = summary
        editorial.save()
        
        return UpdateEditorialMutation(editorial = editorial)

class DeleteEditorialMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    editorial = graphene.Field(EditorialType)

    @classmethod
    def mutate(scl,root,info,id):
        editorial = Editorial.objects.get(id=id)
        editorial.delete()
        
        return 



class CreateAuthorMutation(graphene.Mutation):
    class Arguments:
        name        = graphene.String(required=True)
        last_name   = graphene.String()
        birth_day   = graphene.Date(required=True)
        history     = graphene.String()
        is_active   = graphene.Boolean()
    
    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls,root,info,name,last_name,birth_day,history,is_active):
        author = Author(
            name = name, 
            last_name = last_name,
            birth_day = birth_day,
            history = history,
            is_active = is_active)
        author.save()
        return CreateAuthorMutation(author = author)



class UpdateAuthorMutation(graphene.Mutation):
    class Arguments:
        id          = graphene.ID()
        name        = graphene.String(required=True)
        last_name   = graphene.String()
        birth_day   = graphene.Date(required=True)
        history     = graphene.String()
        is_active   = graphene.Boolean()
    
    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls,root,info,id,name,last_name,birth_day,history,is_active):
        author = Author.objects.get(id=id)
       
        author.name = name, 
        author.last_name = last_name,
        author.birth_day = birth_day,
        author.history = history,
        author.is_active = is_active
        author.save()
        return CreateAuthorMutation(author = author)


class DeleteAuthorMutation(graphene.Mutation):
    class Arguments:
        id          = graphene.ID()
    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls,root,info,id):
        author = Author.objects.get(id=id)
        author.delete()

        return 
  