from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from art.models import Creation, Exhibition, Teaching, RegisterExhibition
from django.utils import timezone
from datetime import datetime, timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
from art.forms import CreationForm, TeachtForm, ExhibitionForm, RegisterExhibitionForm





def art_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('account_login'))
    else:
        creations = Creation.objects.all()
        teaching = Teaching.objects.all()
        exhibition = Exhibition.objects.all()
        registeredexh = RegisterExhibition.objects.all()

        context = {
            'creations' : creations,
            'teaching' : teaching,
            'exhibition' : exhibition,
            'registeredexh' : registeredexh,
            }
        return render(request, 'art/art-home.html', context)

def art_creation(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accounts_login'))
    else:
        if request.method == 'POST':
            form = CreationForm(request.POST)
            if form.is_valid():
                form.save()

        form = CreationForm()
            
        context = {
            'form' : form,
            }
        return render(request, 'art/art-creation.html', context)

def art_teach(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accounts_login'))
    else:
        if request.method == 'POST':
            form = TeachtForm(request.POST)
            if form.is_valid():
                form.save()

        form = TeachtForm()
            
        context = {
            'form' : form,
            }
        return render(request, 'art/art-teach.html', context)

def art_exhibition(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accounts_login'))
    else:
        if request.method == 'POST':
            form = ExhibitionForm(request.POST)
            if form.is_valid():
                form.save()

        form = ExhibitionForm()
            
        context = {
            'form' : form,
            }
        return render(request, 'art/art-exh.html', context)

def art_registerexhibition(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accounts_login'))
    else:
        if request.method == 'POST':
            form = RegisterExhibitionForm(request.POST)
            if form.is_valid():
                form.save()

        form = RegisterExhibitionForm()
            
        context = {
            'form' : form,
            }
        return render(request, 'art/art-rgexh.html', context)
        