from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=128)
    full_description = models.TextField(max_length=512)
    published_date = models.DateField()
    file = models.FileField(upload_to='books/')
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title
