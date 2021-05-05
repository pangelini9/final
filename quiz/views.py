from django.shortcuts import render

from django.contrib.auth.models import User

from .models import Question, Answer, Quiz, Attempt

from datetime import datetime # for the method now()

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
    if student == 4:
        urlTemplate = 'quiz/newAttemptPatrizio.html'
        
    
    return render(request, urlTemplate, context);

def check_attempt(request):
    
    answers = []
    
    score = 0
    
    # create the Quiz object, both in Python and in the DB (it is not formally in the db until the save() is executed, 
    # it only gets an ID at this stage )
    quiz = Quiz.objects.create()
    
    for i in range(1,3):
        answerToQuestion = request.POST.get("quest"+str(i))
        
        answerToQuestionObj = Answer.objects.get(id = answerToQuestion)
        
        answers.append(answerToQuestionObj)
        
        if answerToQuestionObj.correct == True:
            score += 1
        
        quest = answerToQuestionObj.question
        
        # add the Question object corresponding to this Answer to the list of questions of the Quiz object
        # note that the list corresponding to a ManyToMany relationship uses "add" rather than "append"
        quiz.questions.add(quest)
        
    # here we actually store the quiz object in the DB
    quiz.save()

    # create the quiz object, both in Python and in the DB.
    # When creating the attempt, we need to set all the necessary attributes for objects of class Attempt (see models.py)
    # In particular, the Quiz and the User (both foreign keys) have to be set alredy when constructing the Attempt, since they are required
    # the other attribute we can set later    
    attempt = Attempt.objects.create(
        quiz = quiz,
        user = request.user,
        attempt_time = datetime.now(),
        score = score
        )
    # In the above code, we:
    # - Set the created Quiz object as the quiz that has been attempted in this Attempt - it is a foreign key, so I am using the Quiz object
    # - Set the current User as the user who attempted in this Attempt - it is a foreign key, so I am using the User object
    # note that the information on the current User is also stored in the request
    # also note that the User type (the one from Django) has to be imported (see above)
    # - Set the current date and time as the one in which the Attempt was attempted 
    # to read the current date and time, we used the now() method from the class datetime, which has to be imported (see above)
    # - Set the computed score as the one obtained in this Attempt
    
    # Once all attributes have been set, we can finally store the Attempt in the db
    attempt.save()    
    
    context = {"answers" : answers, "score" : score}
    
    urlTemplate = "quiz/check_attempt.html"
    
    return render(request, urlTemplate, context);
    
    
    
    
    
    