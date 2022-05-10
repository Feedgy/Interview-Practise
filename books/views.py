from rest_framework import viewsets

from books.models import Author
from books.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
