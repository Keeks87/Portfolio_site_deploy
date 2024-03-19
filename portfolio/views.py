''' portfolio/views.py'''

# Imports
from django.shortcuts import render
from .models import Project


def portfolio(request):
    return render(request, 'portfolio/portfolio.html', {'projects': projects})

def landing(request):
    return render(request, 'portfolio/landing.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

