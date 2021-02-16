import graphene
#import graphene_django
#from graphene_django import  DjangoListField
from .models import Author,Editorial,Book
from .types import AuthorType,EditorialType,BookType
from .mutations import CreateAuthorMutation, CreateBookMutation, CreateEditorialMutation,UpdateBookMutation,UpdateAuthorMutation,UpdateEditorialMutation,DeleteAuthorMutation,DeleteBookMutation,DeleteEditorialMutation
    

class Query(graphene.ObjectType):
    author      = graphene.Field(AuthorType, id = graphene.Int())
    book        = graphene.Field(BookType, id = graphene.Int())
    editorial   = graphene.Field(EditorialType, id = graphene.Int())

    authors     = graphene.List(AuthorType)
    editorials  = graphene.List(EditorialType)
    books       = graphene.List(BookType)

    def resolve_author(root,info,id):
        return Author.objects.get(pk=id)

    def resolve_book(root,info,id):
        return Book.objects.get(pk=id)

    def resolve_editorial(root,info,id):
        return Editorial.objects.get(pk=id)


    def resolve_authors(root,info):
        return Author.objects.all()

    def resolve_books(root,info):
        return Book.objects.all()

    def resolve_editorials(root,info):
        return Editorial.objects.all()


class Mutation(graphene.ObjectType):

    create_book = CreateBookMutation.Field()
    update_book = UpdateBookMutation.Field()
    delete_book = DeleteBookMutation.Field()

    create_author = CreateAuthorMutation.Field()
    update_author = UpdateAuthorMutation.Field()
    delete_author = DeleteAuthorMutation.Field()

    create_editorial = CreateEditorialMutation.Field()
    update_editorial = UpdateEditorialMutation.Field()
    delete_editorial = DeleteEditorialMutation.Field()
    




schema = graphene.Schema(query= Query,mutation= Mutation)

    