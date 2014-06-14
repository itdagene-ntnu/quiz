from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'quizes'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    text = models.CharField(max_length=200)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    correct_answer = models.OneToOneField(Question,
                                          related_name='correct_answer')
    text = models.CharField(max_length=200)
