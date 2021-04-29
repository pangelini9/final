from django.urls import path

from . import views

app_name = "quiz"

urlpatterns = [
    path("", views.home, name = "home"),
#    path("attempt", views.attempt, name = "attempt"),
    path("attempt/<int:student>", views.attempt, name = "attempt"),
]
