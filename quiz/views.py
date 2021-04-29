from django.shortcuts import render

from .models import Question

import random

# Create your views here.

def home(request):
    return render(request, 'quiz/index.html');


# random.sample(list, number)
# returns a new list that is composed of "number" elements 
# taken at random from the list "list"

def attempt(request, student):
    
    allQuestions = list(Question.objects.all())
    
    questions = random.sample(allQuestions, 2)
    
    pairs = []
    
    for quest in questions:
         answers = quest.answer_set.all()
         
         pair = {
             "question" : quest,
             "answers" : answers
             }
         
         pairs.append(pair)
         
    context = {"pairs" : pairs}
    
    urlTemplate = ""

    if student == 1:
        urlTemplate = 'quiz/newAttemptLorenzo.html'
    if student == 2:
        urlTemplate = 'quiz/newAttemptLuca.html'
    if student == 3:
        urlTemplate = 'quiz/newAttemptTommaso.html'
    
    return render(request, urlTemplate, context);