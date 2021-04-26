from django.db import models

from django.contrib.auth.models import User

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
       
class Quiz(models.Model):
        text = models.CharField(max_length=30)
        questions = models.ManyToManyField(Question)
        def __str__(self):
            return self.text

class Attempt(models.Model):
    ### made by user
    attempt_time = models.DateTimeField()
    # list of selected answers
    score = models.IntegerField()
    feedback = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    
    #which_quiz = models.FilePathField(path=)
