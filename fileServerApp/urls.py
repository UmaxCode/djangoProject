from django.urls import path
from .views import index

urlpatterns = [
    path('blogs/', index, name='index')
]
