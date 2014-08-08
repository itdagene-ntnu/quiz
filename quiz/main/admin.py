from django.contrib import admin
from quiz.admin_helpers import InlineEditLinkMixin
from quiz.main.models import Quiz, Question, Choice, Participant, Answer


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, ]

admin.site.register(Question, QuestionAdmin)


class QuestionInline(InlineEditLinkMixin, admin.TabularInline):
    model = Question
    fields = ('text', 'edit_details')


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline, ]

admin.site.register(Quiz, QuizAdmin)

admin.site.register(Participant)

admin.site.register(Answer)
