from django.shortcuts import render
from .forms import SearchForm

# Create your views here.
def index(request):
    search = SearchForm()
    return render(request, 'house/index.html',{"searchform":search})

def index2(request):
    search = SearchForm()
    return render(request, 'house/index2.html',{"searchform":search})

