from django.urls import path
from .views import *

urlpatterns = [
    path('', base_page, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('driver/<slug:driver_slug>/', show_post, name='driver'),
    path('team/<slug:tm_slug>/', show_team, name='team'),
]