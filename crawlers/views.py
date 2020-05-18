from django.shortcuts import render
from pathlib import Path

# Create your views here.
def index(request):
    return render(request, Path('crawlers/index.html'))

def runSpiders(request):
    return render(request, Path('crawlers/loading.html'))
