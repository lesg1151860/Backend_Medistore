from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# En tu archivo de templates (index.html), podrías tener algo como esto: