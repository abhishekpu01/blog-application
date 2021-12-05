from django.db import models
from django.contrib.auth.models import User
class Contact(models.Model):
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Email = models.EmailField(max_length = 100 , unique = True)
    Phoneno = models.IntegerField(unique = True)
    Query = models.TextField()
    def __str__(self):
        return self.Email

  
class Post(models.Model):
    CATEGORIES = (
        ('public' ,'PUBLIC'),
        ('private' ,'PRIVATE'),
    )
    Title = models.CharField(max_length=50)
    Content = models.TextField()
    Type = models.CharField(max_length=30 , choices = CATEGORIES , default="public")
    Creator = models.ForeignKey(User , on_delete=models.CASCADE)
    Created_on = models.DateTimeField(auto_now_add=True)
    Updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title
