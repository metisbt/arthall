from django.shortcuts import render


def index_view(request):
    return render(request, 'website/index.html')

def panel_view(request):
    return render(request, 'website/panel.html')