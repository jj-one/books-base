from django.db import models

# Create your models here.

class Book(models.Model):

  title = models.CharField(max_length=255)
  number_of_pages = models.IntegerField()
  published_date = models.DateField(auto_now=False, auto_now_add=False)
  quantity = models.IntegerField()

  def __str__(self):
    return self.title
