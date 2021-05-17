from django.shortcuts import render

# Create your views here.
def ShowElements(request):
    return render(request, 'index.html')