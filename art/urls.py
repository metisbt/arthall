from django.urls import path
from art.views import *

app_name = 'art'

urlpatterns = [
    path('',art_view, name='index'),
    path('<int:pid>', art_single, name='single'),
    path('category/<str:cat_name>', art_view, name='category'),
    path('author/<str:author_username>', art_view, name='author'),
]
