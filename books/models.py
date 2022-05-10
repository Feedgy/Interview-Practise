from django.db import models

GENDER_CHOICE = [
    ("F", "Female"),
    ("M", "Male"),
    ("U", "Unknown")
]


# Create your models here.
class Author(models.Model):
    # Agatha Christie 1NF
    fullname = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)


class Book(models.Model):
    title = models.CharField(max_length=1000, help_text="Name of the book")
    # 2 NF
    genre = models.CharField(max_length=100, help_text="genre of the book (Horror, Drama, ...)")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Library(models.Model):
    name = models.CharField(max_length=100, help_text="name of the library")
    country = models.CharField(max_length=100, help_text="description of where is the library FR")
