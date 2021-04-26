from django.shortcuts import render

import random

# Create your views here.

def home(request):
    return render(request, 'quiz/index.html');


# random.sample(list, number)
# returns a new list that is composed of "number" elements 
# taken at random from the list "list"

