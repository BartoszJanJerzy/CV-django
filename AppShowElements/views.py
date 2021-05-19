from django.shortcuts import render
from .models import Kurs, Project

# Create your views here.
def ShowElements(request):
    kurs = Kurs.objects.all()
    project = Project.objects.all()
    return render(request, 'index.html', {'kurs':kurs, 'project':project})