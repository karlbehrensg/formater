from django.urls import path
from . import views

app_name = 'karate'

urlpatterns = [
    path('', views.json_fields, name='json_fields'),
]