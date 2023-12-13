# import path and map views to urls
from django.urls import path
from . import views

# define url patterns
urlpatterns = [
    path('', views.index, name='index'),
]