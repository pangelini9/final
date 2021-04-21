from django.db import models

# Create your models here.

from django.db import models 


class Answer(models.Models):
        text = models.CharField(max_length=30);
        correct = models.BooleanField();
        question = models.ForeignKey(Question, on_delete=models.CASCADE);
        def __str__(self):
            return self.text
       
        
class Question(models.Models):
        text = models.CharField(max_length=30);
        def __str__(self):
            return self.text
    