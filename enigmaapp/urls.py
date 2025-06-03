# enigmaapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('custom/', views.custom_page, name='custom_page'),
]