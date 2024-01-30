from django.db import models


class Books(models.Model):

    def __str__(self) -> str:
        return self.Bookname
    
    Bookname = models.CharField(max_length = 600)
    image= models.ImageField(default='default.jpg',upload_to='book_photo/')
    Authorname = models.CharField(max_length = 600)
    Ratings = models.IntegerField(null=True)
    Description = models.CharField(max_length = 600)
    Price = models.IntegerField(null=True)
    
    

