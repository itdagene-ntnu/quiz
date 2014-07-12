from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from quiz.main.models import Quiz


def landing(req):
    current_quizes = Quiz.objects.filter(start__lte=timezone.now(),
                                         end__gte=timezone.now())
    if len(current_quizes) > 0:
        return render(req, 'landing.html', {'current_quiz': current_quizes[0]})
    else:
        return render(req, 'no_quiz.html')


def quiz(req, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    return HttpResponse("This is quiz: %s" % quiz)