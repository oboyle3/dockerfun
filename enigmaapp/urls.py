# enigmaapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('custom/', views.custom_page, name='custom_page'),
    path('about/', views.about, name='about'),
    path('algorithms/', views.algorithms, name='algorithms'),
    path('playground/', views.playground, name='playground'),
    path('history/', views.history, name='history'),
]