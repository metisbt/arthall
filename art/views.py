from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from art.models import Creation, Exhibition, Teaching, RegisterExhibition
from django.utils import timezone
from datetime import datetime, timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
from art.forms import CreationForm, TeachtForm, ExhibitionForm, RegisterExhibitionForm





def art_view(request, **kwargs):
    creations = Creation.objects.all()
    teach = Teaching.objects.all()
    exhibition = Exhibition.objects.all()
    registeredexh = RegisterExhibition.objects.all()

    context = {
        'creations' : creations,
        'teach' : teach,
        'exhibition' : exhibition,
        'registeredexh' : registeredexh,
        }
    return render(request, 'art/art-home.html', context)
    
def art_teach(request):
    form = TeachtForm()
         
    context = {
        'form' : form,
        }
    return render(request, 'art/art-teach.html', context)

def art_exhibition(request):
    form = ExhibitionForm()
         
    context = {
        'form' : form,
        }
    return render(request, 'art/art-exh.html', context)

def art_registerexhibition(request):
    form = RegisterExhibitionForm()
         
    context = {
        'form' : form,
        }
    return render(request, 'art/art-rgexh.html', context)
        
def art_search(request):
    creations = Creation.objects.filter(status=1)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            creations= creations.filter(content__contains=s)

    context = {'creations' : creations}
    return render(request, 'art/art-home.html', context)