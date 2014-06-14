from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=include('quiz.main.urls'),
    ),
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
)
