from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def base_page(request):
    drivers = Drivers.objects.all()
    context = {
        'drivers': drivers,
        'menu': menu,
        'title': 'Main Page',
        'team_selected': 0
    }
    return render(request, 'season/base_page.html', context=context)


def show_post(request, driver_slug):
    drivers = get_object_or_404(Drivers, slug=driver_slug)
    context = {
        'drivers': drivers,
        'menu': menu,
        'title': drivers.name,
        'team_selected': drivers.teams_id,
    }
    print(context)
    return render(request, 'season/driver.html', context=context)


def show_team(request, tm_slug):
    team = Teams.objects.get(slug=tm_slug)
    drivers = Drivers.objects.filter(teams_id=team.pk)


    context = {
        'drivers': drivers,
        'menu': menu,
        'title': team.name,
        'team_selected': team.pk
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
