from django.urls import path
from .views import ShowElements

urlpatterns = [
    path('', ShowElements, name='show-elements')
]