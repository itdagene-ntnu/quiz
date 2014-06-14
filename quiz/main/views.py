from django.shortcuts import render


def landing(req):
    return render(req, 'landing.html')
