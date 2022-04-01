from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def base_page(request):
    drivers = Drivers.objects.all()
    teams = Teams.objects.all()
    context = {
        'drivers': drivers,
        'teams': teams,
        'menu': menu,
        'title': 'Main Page',
        'team_selected': 0
    }
    return render(request, 'season/base_page.html', context=context)


def show_post(request, t_id):
    drivers = Drivers.objects.filter(id=t_id)
    teams = Teams.objects.all()

    if len(drivers) == 0:
        raise Http404()

    context = {
        'drivers': drivers,
        'teams': teams,
        'menu': menu,
        'title': 'Driver',
        'team_selected': t_id
    }
    return render(request, 'season/base_page.html', context=context)


def about(request):
    return HttpResponse("About")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponse("Стараца не найдена")
