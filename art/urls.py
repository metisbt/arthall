from django.urls import path
from art.views import *

app_name = 'art'

urlpatterns = [
    path('',art_view, name='index'),
    path('creation', art_creation, name='creation'),
    path('teach', art_teach, name='teach'),
    path('exhibition', art_exhibition, name='exhibition'),
    path('registerexhibition', art_registerexhibition, name='registerexhibition'),
]
