from django.conf.urls import patterns, url

urlpatterns = patterns(
    'quiz.main.views',
    url(
        regex=r'^$',
        view='landing',
        name='landing'
    ),
)
