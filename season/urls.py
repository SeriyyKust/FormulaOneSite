from django.urls import path
from .views import *

urlpatterns = [
    path('', DriverHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('driver/<slug:driver_slug>/', ShowPost.as_view(), name='driver'),
    path('team/<slug:tm_slug>/', DriversTeams.as_view(), name='team'),
]