from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User

# Create your models here.

class Ebook(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=20)
    description = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return str(self.rating)



