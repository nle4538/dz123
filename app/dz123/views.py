from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import datetime


def index(request):
    template = loader.get_template("dz123/index.html")
    context = {'title': 'Главная страница',
               'pages': [('writers', 'Писатели'),
                         ('books', 'Книги'),
                         ]}
    return HttpResponse(template.render(context, request))


from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Главная</h1><p>Добро пожаловать на главную страницу!</p>')

def writers(request):
    return HttpResponse('<h1>Писатели</h1><p>Здесь вы можете узнать о писателях.</p>')

def books(request):
    return HttpResponse('<h1>Топ лучших книг</h1><p>Здесь представлен топ лучших книг.</p>')
