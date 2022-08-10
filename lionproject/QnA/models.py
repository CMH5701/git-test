from django.db import models
from distutils.command.upload import upload


# Create your models here.
class Qna(models.Model):    
    question = models.CharField(max_length = 200)
    q_date = models.DateTimeField('data published')
    q_photo = models.ImageField(upload_to = 'q_images/', blank =True ,null = True)
    hashtags = models.ManyToManyField('Hashtag' , blank = True)
    
    def __str__(self):
        return self.question

class Comment(models.Model) :
    def __str__(self) :
        return self.text

    qna_id = models.ForeignKey(Qna, on_delete = models.CASCADE, related_name='comments') 
    text = models.CharField(max_length=50)

class Hashtag(models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name
        