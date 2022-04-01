from django.shortcuts import render
from django.http import HttpResponse


def base_page(request):
    return HttpResponse("Main Page!")


def categories(request, catid):
    return HttpResponse(f"<h1>Category</h1><p>{catid}</p>")
