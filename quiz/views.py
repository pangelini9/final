from django.shortcuts import render

from .models import Question, Answer, Quiz, Attempt

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
    
    # create the quiz object, both in Python and in the DB (it is not formally in the db till the save() is executed, 
    # it only gets an ID at this stage )
    quiz = Quiz.objects.create()
    
    for i in range(1,3):
        answerToQuestion = request.POST.get("quest"+str(i))
        
        answerToQuestionObj = Answer.objects.get(id = answerToQuestion)
        
        answers.append(answerToQuestionObj)
        
        if answerToQuestionObj.correct == True:
            score += 1
        
        quest = answerToQuestion.question
        
        # add the Question object corresponding to this Answer to the list of questions of the Quiz object
        quiz.questions.add(quest)
        
    # store the quiz object in the DB
    quiz.save()

    # create the quiz object, both in Python and in the DB
    attempt = Attempt.objects.create()
    # set the created Quiz object as the quiz that has been attempted in this Attempt
    attempt.quiz = quiz
    
    context = {"answers" : answers, "score" : score}
    
    urlTemplate = "quiz/check_attempt.html"
    
    return render(request, urlTemplate, context);
    
    
    
    
    
    