from django.contrib import admin
from quiz.main.models import Quiz, Question, Choice

admin.site.register([Quiz, Question, Choice])
