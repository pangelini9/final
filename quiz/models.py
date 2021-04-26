from django.db import models

# Create your models here.

class Question(models.Model):
        text = models.CharField(max_length=60);
        def __str__(self):
            return self.text

class Answer(models.Model):
        text = models.CharField(max_length=60);
        correct = models.BooleanField();
        question = models.ForeignKey(Question, on_delete=models.CASCADE);
        def __str__(self):
            return self.text
       
        