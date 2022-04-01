from django.shortcuts import render
from django.http import HttpResponse


def base_page(request):
    return HttpResponse("Main Page!")


def teams(request, tid):
    return HttpResponse(f"<h1>Category</h1><p>{tid}</p>")


def pageNotFound(request, exception):
    return HttpResponse("Стараца не найдена")
