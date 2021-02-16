from django.urls import path
from library.schema import schema
from graphene_django.views import GraphQLView

urlpatterns = [
    path('graph',GraphQLView.as_view(graphiql=True, schema = schema))
]
