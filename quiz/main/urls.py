from django.conf.urls import patterns, url

urlpatterns = patterns(
    'quiz.main.views',
    url(
        regex=r'^quiz/(?P<quiz_id>\d+)/$',
        view='quiz',
        name='view-quiz'
    ),
    url(
        regex=r'^$',
        view='landing',
        name='landing'
    ),
)