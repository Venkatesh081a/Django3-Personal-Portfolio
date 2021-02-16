from django.shortcuts import render
from .models import Project


def home(request):
    projects_db = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects_db})
