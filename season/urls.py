from django.urls import path
from .views import *

urlpatterns = [
    path('season/', base_page),
    path('cats/<int:catid>/', categories)
]