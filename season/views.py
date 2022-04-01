from django.shortcuts import render
from django.http import HttpResponse
from .models import *

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def base_page(request):
    drivers = Drivers.objects.all()
    return render(request, 'season/base_page.html', {'title': 'Season 2022', 'menu': menu, 'drivers': drivers})


def teams(request, tid):
    return HttpResponse(f"<h1>Category</h1><p>{tid}</p>")


def pageNotFound(request, exception):
    return HttpResponse("Стараца не найдена")
