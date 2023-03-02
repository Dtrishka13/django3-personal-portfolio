from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all() #импортирование всех записей о проектах из базы данных
    return render(request, 'portfolio/home.html', {'projects' : projects})
