from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'quizes'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    correct_answer = models.BooleanField(default=False)
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text
