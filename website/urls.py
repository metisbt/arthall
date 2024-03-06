from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('',index_view, name='home'),
    path('dashboard',index_view, name='panel'),
]
