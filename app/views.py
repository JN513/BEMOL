from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import PersonForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def cadastrados(request):
    return render(request, 'cadastrados.html')

def form(request):
    data = {}
    data['form'] = PersonForm()
    return render(request, 'form.html', data)

def create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/create')
    #else:
    #   form = PersonForm()
    #return render(request, 'form.html', {'form': form} )