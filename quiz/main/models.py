from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'quizes'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    text = models.TextField()

    def __unicode__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    correct_answer = models.BooleanField(default=False)
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text


class Participant(models.Model):
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=25)

    def __unicode__(self):
        return self.email


class Answer(models.Model):
    question = models.ForeignKey(Question)
    choice = models.ForeignKey(Choice)
    participant = models.ForeignKey(Participant)