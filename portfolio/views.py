from django.shortcuts import render
from .models import Project, Experiencia

def home(request):
    projects = Project.objects.all()
    return render(request,'home.html',{'projects':projects})


from django.shortcuts import render
from .models import Project, Experiencia

def home(request):
    projects = Project.objects.all()
    experiencias = Experiencia.objects.all()  # Obtiene todas las experiencias
    return render(request, 'home.html', {'projects': projects, 'experiencias': experiencias})
