from django.urls import path
from .views import *

urlpatterns = [
    path('', base_page, name='home'),
    path('teams/<int:tid>/', teams)
]