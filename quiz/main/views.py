from django.shortcuts import render
from django.utils import timezone
from quiz.main.models import Quiz


def landing(req):
    current_quiz = Quiz.objects.get(start__lte=timezone.now(),
                                    end__gte=timezone.now())
    print current_quiz
    return render(req, 'landing.html', {'current_quiz': current_quiz})
