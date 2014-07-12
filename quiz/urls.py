from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(
        regex=r'^admin/',
        view=include(admin.site.urls)
    ),
    url(
        regex=r'^',
        view=include('quiz.main.urls'),
        name='main'
    ),
)
