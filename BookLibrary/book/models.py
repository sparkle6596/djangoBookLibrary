from django.db import models

# Create your models here.

class Books(models.Model):
    book_name=models.CharField(max_length=70,unique=True)
    author=models.CharField(max_length=15)
    category=models.CharField(max_length=50)
    price=models.IntegerField()
    copies=models.IntegerField()

    def __str__(self):
        return self.book_name








